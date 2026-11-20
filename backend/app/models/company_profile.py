
import uuid
from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    CheckConstraint,
    ForeignKey,
    func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db_base import Base


class CompanyProfile(Base):
    __tablename__ = "company_profiles"

    __table_args__ = (
        CheckConstraint(
            "verification_status IN ('PENDING', 'VERIFIED', 'REJECTED')",
            name="ck_company_profiles_verification_status"
        ),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True
    )

    company_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    registration_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    company_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    website_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    logo_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    industry: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    verification_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="PENDING"
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
