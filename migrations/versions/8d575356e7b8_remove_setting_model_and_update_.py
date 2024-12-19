"""Remove Setting model and update Category model

Revision ID: 8d575356e7b8
Revises: 402669e3855e
Create Date: 2024-12-18 16:18:58.007429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d575356e7b8'
down_revision = '402669e3855e'
branch_labels = None
depends_on = None


def upgrade():
    # Drop the settings table
    op.drop_table('setting')

    # Add columns with default values and then remove the default
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timer_duration', sa.Integer(), nullable=False, server_default='300'))
        batch_op.add_column(sa.Column('questions_per_quiz', sa.Integer(), nullable=False, server_default='10'))

    # Remove the default value
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.alter_column('timer_duration', server_default=None)
        batch_op.alter_column('questions_per_quiz', server_default=None)


def downgrade():
    # Drop columns
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_column('questions_per_quiz')
        batch_op.drop_column('timer_duration')

    # Re-create the settings table
    op.create_table('setting',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('value', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
