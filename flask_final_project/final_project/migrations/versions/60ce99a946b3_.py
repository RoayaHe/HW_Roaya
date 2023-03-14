"""empty message

Revision ID: 60ce99a946b3
Revises: 4dec6292e35b
Create Date: 2023-01-30 23:58:44.153596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60ce99a946b3'
down_revision = '4dec6292e35b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('video_link', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.drop_column('video_link')

    # ### end Alembic commands ###
