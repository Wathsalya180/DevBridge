
import uuid
from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    BigInteger,
    CheckConstraint,
    ForeignKey,
    func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db_base import Base


class StudentVerification(Base):
    __tablename__ = "student_verifications"

    
    __table_args__ = (
        CheckConstraint(
            "document_type IN ('STUDENT_ID', 'ENROLLMENT_LETTER', 'OTHER')",
            name="ck_student_verifications_document_type"
        ),
        CheckConstraint(
            "status IN ('PENDING', 'APPROVED', 'REJECTED')",
            name="ck_student_verifications_status"
        ),
        CheckConstraint(
            "file_size_bytes >= 0",
            name="ck_student_verifications_file_size"
        ),
        CheckConstraint(
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
            name="ck_student_verifications_review_consistency"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    developer_user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("developer_profiles.user_id"),
        nullable=False
    )

    document_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    file_url: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    original_file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    file_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    file_size_bytes: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="PENDING"
    )

    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    reviewed_by: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )

    reviewed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    rejection_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
