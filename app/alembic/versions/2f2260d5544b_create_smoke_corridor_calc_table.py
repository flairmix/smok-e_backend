"""create smoke_corridor_calc table

Revision ID: 2f2260d5544b
Revises: 
Create Date: 2023-11-20 00:10:34.218137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f2260d5544b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    os.create_table(
        'smoke_corridor_calc', 
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String),
        sa.Column('description', sa.String)
    )


def downgrade() -> None:
    pass


