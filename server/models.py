from database import Base
import datetime
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime
from sqlalchemy.sql.expression import null

# Create a Table for News models for the database that contain Youtube video Info + Transcript
class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    transcript = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    title = Column(String(255), nullable=False)
    video_id = Column(String(255), nullable=False)
    published_at = Column(DateTime, nullable=False)
    # Create and Update Time should be auto now True
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"<News title={self.title}>"
