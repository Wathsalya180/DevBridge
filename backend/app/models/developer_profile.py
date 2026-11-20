
import uuid
from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    CheckConstraint,
    UniqueConstraint,
    ForeignKey,
    func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db_base import Base


class DeveloperProfile(Base):
    __tablename__ = "developer_profiles"

    __table_args__ = (
        CheckConstraint(
            "developer_type IN ('STUDENT', 'PROFESSIONAL')",
            name="ck_developer_profiles_type"
        ),
        UniqueConstraint(
            "username",
            name="uq_developer_profiles_username"
        ),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    developer_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    university_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    bio: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    profile_image_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    portfolio_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    instagram_url: Mapped[str | None] = mapped_column(
        String(255),
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
