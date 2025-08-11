"""create positions table

Revision ID: 08fa55917815
Revises: 6438ea463727
Create Date: 2025-07-25 13:24:31.820772

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "08fa55917815"
down_revision: Union[str, Sequence[str], None] = "6438ea463727"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "positions",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("bot_group_id", sa.Integer, sa.ForeignKey("bot_groups.id"), nullable=False),
        sa.Column("add_ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("end_ts", sa.DateTime(timezone=True)),
        sa.Column("modified_ts", sa.DateTime(timezone=True)),
        sa.Column("bot_start_ts", sa.DateTime(timezone=True)),
        sa.Column("token", sa.String(16), nullable=False),
        sa.Column("order_name", sa.String(32), nullable=False, unique=True),
        sa.Column("leverage", sa.Numeric, nullable=False),
        sa.Column("restart", sa.Boolean, nullable=False, default=False),
        sa.column("is_active", sa.Boolean, nullable=False, default=False),
        sa.Column("exit_on_empty", sa.Boolean, nullable=False, default=False),
        sa.Column("comment", sa.String(255)),
        sa.Column("leftover_qty", sa.Numeric),
        sa.Column("orders_config", postgresql.JSONB, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("positions")
