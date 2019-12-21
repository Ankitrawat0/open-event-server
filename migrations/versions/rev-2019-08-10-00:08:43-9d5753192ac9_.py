"""unique constraint on feedback

Revision ID: 9d5753192ac9
Revises: f5c3a4fd23fb
Create Date: 2019-08-10 00:08:43.135975

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '9d5753192ac9'
down_revision = 'f5c3a4fd23fb'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('session_user_uc', 'feedback', ['session_id', 'user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('session_user_uc', 'feedback', type_='unique')
    # ### end Alembic commands ###