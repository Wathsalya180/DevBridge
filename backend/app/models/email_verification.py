
import uuid
from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    CheckConstraint,
    ForeignKey,
    Index,
    func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db_base import Base


class EmailVerification(Base):
    __tablename__ = "email_verifications"

    __table_args__ = (
        CheckConstraint(
            "verification_type IN ('PRIMARY_EMAIL', 'UNIVERSITY_EMAIL')",
            name="ck_email_verifications_type"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    verification_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    token_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    invalidated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )


# Allow only one unverified, non-invalidated challenge
# for each user and verification purpose.
Index(
    "uq_email_verifications_active_user_purpose",
    EmailVerification.user_id,
    EmailVerification.verification_type,
    unique=True,
    postgresql_where=(
        EmailVerification.verified_at.is_(None)
        & EmailVerification.invalidated_at.is_(None)
    )
)
