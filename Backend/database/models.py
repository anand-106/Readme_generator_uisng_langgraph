
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, Integer, func

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=False)
    avatarUrl = Column(String, nullable=True)
    githubToken = Column(String, nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    repositories = relationship("Repository", back_populates="user")


class Repository(Base):
    __tablename__ = "Repository"
    id = Column(String, primary_key=True)
    userId = Column(String, ForeignKey("User.id"))
    name = Column(String, nullable=False)
    fullname = Column(String, unique=True, nullable=False)
    url = Column(String, nullable=False)
    htmlUrl = Column(String, nullable=False)
    isPrivate = Column(Boolean, nullable=False)
    stars = Column(Integer, default=0)
    forks = Column(Integer, default=0)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    user = relationship("User", back_populates="repositories")
    webhook = relationship("Webhook", back_populates="repository", uselist=False)


class Webhook(Base):
    __tablename__ = "Webhook"
    id = Column(String, primary_key=True)
    secret = Column(String, unique=True, nullable=False)
    webhookUrl = Column(String, nullable=False)
    repoId = Column(String, ForeignKey("Repository.id"), unique=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    repository = relationship("Repository", back_populates="webhook")
