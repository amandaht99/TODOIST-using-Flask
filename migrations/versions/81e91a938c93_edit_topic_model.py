"""edit Topic Model

Revision ID: 81e91a938c93
Revises: 3193650a26ac
Create Date: 2023-04-14 14:01:12.600447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81e91a938c93'
down_revision = '3193650a26ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topic', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=1024), nullable=True))
        batch_op.drop_column('slug')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topic', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.VARCHAR(length=80), nullable=True))
        batch_op.drop_column('description')

    # ### end Alembic commands ###