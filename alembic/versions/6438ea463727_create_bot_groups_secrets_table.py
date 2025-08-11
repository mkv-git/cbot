"""create bot_groups_secrets table

Revision ID: 6438ea463727
Revises: a9696e44412d
Create Date: 2025-07-25 13:24:23.378935

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6438ea463727"
down_revision: Union[str, Sequence[str], None] = "a9696e44412d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bot_group_secrets",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("bot_group_id", sa.Integer, sa.ForeignKey("bot_groups.id"), nullable=False),
        sa.Column("add_ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("permission", sa.String(2), nullable=False),
        sa.Column("api_key", sa.String(64), unique=True, nullable=False),
        sa.Column("api_secret", sa.String(64), unique=True, nullable=False),
        sa.Column('expiration_ts', sa.DateTime(timezone=True)),
    )


def downgrade() -> None:
    op.drop_table("bot_group_secrets")
