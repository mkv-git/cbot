"""create bot_groups table

Revision ID: dbe07de078af
Revises:
Create Date: 2025-07-21 18:37:34.608940

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dbe07de078af"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bot_groups",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("add_ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("modified_ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("group_name", sa.String(16), nullable=False, unique=True),
        sa.Column("uid", sa.Integer, nullable=False),
        sa.Column("exchange", sa.String(16), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("bot_groups")
