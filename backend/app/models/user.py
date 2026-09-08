import uuid
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
import enum


class UserRole(str, enum.Enum):
    ADMIN_BAPPENDA = "admin_bappenda"
    PETUGAS_PENGAWASAN = "petugas_pengawasan"
    VIEWER = "viewer"


class User(Base):
    """PRD table: users — accounts + role for RBAC (Module 1)."""
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.VIEWER)
    is_active: Mapped[bool] = mapped_column(default=True)
