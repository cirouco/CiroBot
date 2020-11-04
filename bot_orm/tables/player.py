from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import attribute_mapped_collection

from bot_orm.session import bot_declarative_base


class Player(bot_declarative_base):
    """Represents a player taking part in inhouse games"""

    __tablename__ = "player"

    # Discord account info
    id = Column(BigInteger, primary_key=True)

    # One player object per server_id
    server_id = Column(BigInteger, primary_key=True)

    # Player nickname and team as defined by themselves
    name = Column(String)
    team = Column(String)

    ratings = relationship(
        "PlayerRating",
        collection_class=attribute_mapped_collection("role"),
        backref="player",
        cascade="all, delete-orphan",
    )

    # ORM relationship to the GameParticipant table
    participant_objects = relationship("GameParticipant", viewonly=True)

    def __repr__(self):
        return f"<Player: {self.id=} | {self.name=}>"
