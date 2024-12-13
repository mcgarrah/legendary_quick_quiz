"""Add no_shuffle to Question model

Revision ID: 402669e3855e
Revises: 
Create Date: 2024-12-11 18:58:55.493161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '402669e3855e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('no_shuffle', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('no_shuffle')

    # ### end Alembic commands ###