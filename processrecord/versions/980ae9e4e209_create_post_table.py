"""create post table

Revision ID: 980ae9e4e209
Revises: 
Create Date: 2022-04-16 20:36:15.456992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980ae9e4e209'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
