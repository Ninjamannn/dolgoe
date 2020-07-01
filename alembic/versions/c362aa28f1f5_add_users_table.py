"""Add users table

Revision ID: c362aa28f1f5
Revises: f84206db0560
Create Date: 2020-07-01 21:34:08.161846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c362aa28f1f5'
down_revision = 'f84206db0560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('point', sa.Integer(), nullable=True),
    sa.Column('secret', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###