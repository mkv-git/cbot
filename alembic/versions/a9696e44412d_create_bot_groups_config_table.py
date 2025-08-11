"""create bot_groups_config table

Revision ID: a9696e44412d
Revises: dbe07de078af
Create Date: 2025-07-25 13:24:15.596218

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a9696e44412d"
down_revision: Union[str, Sequence[str], None] = "dbe07de078af"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bot_group_config",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("bot_group_id", sa.Integer, sa.ForeignKey("bot_groups.id"), nullable=False),
        sa.Column("public_ws_port", sa.SmallInteger, unique=True, nullable=False),
        sa.Column("order_ws_port", sa.SmallInteger, unique=True, nullable=False),
        sa.Column("trade_ws_port", sa.SmallInteger, unique=True, nullable=False),
        sa.Column("rest_api_ws_port", sa.SmallInteger, unique=True, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("bot_group_config")
