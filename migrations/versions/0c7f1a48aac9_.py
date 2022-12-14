"""empty message

Revision ID: 0c7f1a48aac9
Revises: 2d2fc3e826af
Create Date: 2019-12-15 21:49:02.167122

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c7f1a48aac9'
down_revision = '2d2fc3e826af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'can_use_custom_domain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('can_use_custom_domain', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
