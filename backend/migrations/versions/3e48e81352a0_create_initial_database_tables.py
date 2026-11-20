
"""Create initial database tables

Revision ID: 3e48e81352a0
Revises:
Create Date: 2026-11-20 15:50:17.070709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e48e81352a0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('role', sa.String(length=20), nullable=False),
        sa.Column('account_status', sa.String(length=20), nullable=False),
        sa.Column('email_verified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.CheckConstraint(
            "account_status IN ('ACTIVE', 'SUSPENDED', 'DEACTIVATED')",
            name='ck_users_account_status'
        ),
        sa.CheckConstraint(
            "role IN ('DEVELOPER', 'COMPANY', 'ADMIN')",
            name='ck_users_role'
        ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        'uq_users_email_lower',
        'users',
        [sa.literal_column('lower(email)')],
        unique=True
    )

    op.create_table(
        'company_profiles',
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('company_name', sa.String(length=200), nullable=False),
        sa.Column('registration_number', sa.String(length=100), nullable=True),
        sa.Column('company_email', sa.String(length=255), nullable=False),
        sa.Column('website_url', sa.String(length=255), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('logo_url', sa.Text(), nullable=True),
        sa.Column('industry', sa.String(length=100), nullable=False),
        sa.Column('verification_status', sa.String(length=20), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.CheckConstraint(
            "verification_status IN ('PENDING', 'VERIFIED', 'REJECTED')",
            name='ck_company_profiles_verification_status'
        ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('user_id')
    )

    op.create_table(
        'developer_profiles',
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('full_name', sa.String(length=150), nullable=False),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('developer_type', sa.String(length=20), nullable=False),
        sa.Column('university_email', sa.String(length=255), nullable=True),
        sa.Column('bio', sa.Text(), nullable=True),
        sa.Column('profile_image_url', sa.Text(), nullable=True),
        sa.Column('github_url', sa.String(length=255), nullable=True),
        sa.Column('linkedin_url', sa.String(length=255), nullable=True),
        sa.Column('portfolio_url', sa.String(length=255), nullable=True),
        sa.Column('instagram_url', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.CheckConstraint(
            "developer_type IN ('STUDENT', 'PROFESSIONAL')",
            name='ck_developer_profiles_type'
        ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('username', name='uq_developer_profiles_username')
    )

    op.create_table(
        'email_verifications',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('verification_type', sa.String(length=30), nullable=False),
        sa.Column('token_hash', sa.String(length=255), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('verified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('invalidated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.CheckConstraint(
            "verification_type IN ('PRIMARY_EMAIL', 'UNIVERSITY_EMAIL')",
            name='ck_email_verifications_type'
        ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        'uq_email_verifications_active_user_purpose',
        'email_verifications',
        ['user_id', 'verification_type'],
        unique=True,
        postgresql_where=sa.text(
            'verified_at IS NULL AND invalidated_at IS NULL'
        )
    )

    op.create_table(
        'student_verifications',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('developer_user_id', sa.UUID(), nullable=False),
        sa.Column('document_type', sa.String(length=30), nullable=False),
        sa.Column('file_url', sa.Text(), nullable=False),
        sa.Column('original_file_name', sa.String(length=255), nullable=False),
        sa.Column('file_type', sa.String(length=100), nullable=False),
        sa.Column('file_size_bytes', sa.BigInteger(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('submitted_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('reviewed_by', sa.UUID(), nullable=True),
        sa.Column('reviewed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('rejection_reason', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.CheckConstraint(
            """
            (
                status = 'PENDING'
                AND reviewed_by IS NULL
                AND reviewed_at IS NULL
                AND rejection_reason IS NULL
            )
            OR
            (
                status = 'APPROVED'
                AND reviewed_by IS NOT NULL
                AND reviewed_at IS NOT NULL
                AND rejection_reason IS NULL
            )
            OR
            (
                status = 'REJECTED'
                AND reviewed_by IS NOT NULL
                AND reviewed_at IS NOT NULL
                AND rejection_reason IS NOT NULL
                AND length(trim(rejection_reason)) > 0
            )
            """,
            name='ck_student_verifications_review_consistency'
        ),
        sa.CheckConstraint(
            "document_type IN ('STUDENT_ID', 'ENROLLMENT_LETTER', 'OTHER')",
            name='ck_student_verifications_document_type'
        ),
        sa.CheckConstraint(
            "status IN ('PENDING', 'APPROVED', 'REJECTED')",
            name='ck_student_verifications_status'
        ),
        sa.CheckConstraint(
            'file_size_bytes >= 0',
            name='ck_student_verifications_file_size'
        ),
        sa.ForeignKeyConstraint(
            ['developer_user_id'],
            ['developer_profiles.user_id']
        ),
        sa.ForeignKeyConstraint(
            ['reviewed_by'],
            ['users.id']
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table('student_verifications')

    op.drop_index(
        'uq_email_verifications_active_user_purpose',
        table_name='email_verifications',
        postgresql_where=sa.text(
            'verified_at IS NULL AND invalidated_at IS NULL'
        )
    )

    op.drop_table('email_verifications')
    op.drop_table('developer_profiles')
    op.drop_table('company_profiles')

    op.drop_index(
        'uq_users_email_lower',
        table_name='users'
    )

    op.drop_table('users')
