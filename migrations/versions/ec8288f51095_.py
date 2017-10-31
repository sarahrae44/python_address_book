"""empty message

Revision ID: ec8288f51095
Revises: bdb2d375ffdf
Create Date: 2017-10-30 23:21:09.214972

"""

# revision identifiers, used by Alembic.
revision = 'ec8288f51095'
down_revision = 'bdb2d375ffdf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('live', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'live')
    # ### end Alembic commands ###
