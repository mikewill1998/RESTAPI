"""add content colun to post table

Revision ID: 6be83e29465e
Revises: 980ae9e4e209
Create Date: 2022-04-16 20:43:26.055111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6be83e29465e'
down_revision = '980ae9e4e209'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
