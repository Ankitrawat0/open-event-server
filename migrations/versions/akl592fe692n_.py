"""empty message

Revision ID: akl592fe692n
Revises: 2453426d2a35
Create Date: 2018-08-06 01:36:13.491209

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'akl592fe692n'
down_revision = '2453426d2a35'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_favourite_events', sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_favourite_events', 'deleted_at')
    # ### end Alembic commands ###