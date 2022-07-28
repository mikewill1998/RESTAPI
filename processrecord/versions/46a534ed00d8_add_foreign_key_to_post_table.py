"""add foreign key to post table

Revision ID: 46a534ed00d8
Revises: efdc54bae942
Create Date: 2022-04-16 21:06:42.035056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46a534ed00d8'
down_revision = 'efdc54bae942'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_table('posts', 'owner_id')
    pass
