"""create orders table

Revision ID: 51b711370cd3
Revises: 08fa55917815
Create Date: 2025-07-25 15:23:43.216220

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "51b711370cd3"
down_revision: Union[str, Sequence[str], None] = "08fa55917815"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("position_id", sa.Integer, sa.ForeignKey("positions.id"), nullable=False),
        sa.Column("position_type", sa.SmallInteger, nullable=False),
        sa.Column("add_ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("modified_ts", sa.DateTime(timezone=True)),
        sa.Column("is_active", sa.Boolean, nullable=False, default=False),
        sa.Column("terminate", sa.Boolean, nullable=False, default=False),
        sa.Column("postponed", sa.Boolean, nullable=False, default=False),
        sa.Column("pnl", sa.Numeric),
        sa.Column("stop_loss", sa.Numeric),
        sa.Column("entry_price", sa.Numeric),
        sa.Column("sell_activation_price", sa.Numeric),
        sa.Column("buy_ts", sa.DateTime(timezone=True)),
        sa.Column("buy_qty", sa.Numeric),
        sa.Column("buy_price", sa.Numeric),
        sa.Column("buy_status", sa.String(16)),
        sa.Column("buy_order_id", sa.String(64)),
        sa.Column("buy_order_link_id", sa.String(64)),
        sa.Column("sell_ts", sa.DateTime(timezone=True)),
        sa.Column("sell_qty", sa.Numeric),
        sa.Column("sell_price", sa.Numeric),
        sa.Column("sell_status", sa.String(16)),
        sa.Column("sell_order_id", sa.String(64)),
        sa.Column("sell_order_link_id", sa.String(64)),
        sa.Column("comment", sa.String(255)),
    )


def downgrade() -> None:
    op.drop_table("orders")
