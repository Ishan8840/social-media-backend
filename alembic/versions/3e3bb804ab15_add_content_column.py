"""add content column

Revision ID: 3e3bb804ab15
Revises: a9cb814fdd90
Create Date: 2025-08-07 12:59:38.324018

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3e3bb804ab15"
down_revision: Union[str, Sequence[str], None] = "a9cb814fdd90"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
