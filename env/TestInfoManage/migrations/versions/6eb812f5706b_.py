"""empty message

Revision ID: 6eb812f5706b
Revises: de67c6ed6245
Create Date: 2018-08-20 10:23:12.116476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eb812f5706b'
down_revision = 'de67c6ed6245'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('projectname', sa.String(length=20), nullable=False),
    sa.Column('projectdescription', sa.String(length=100), nullable=True),
    sa.Column('creator', sa.String(length=20), nullable=False),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('projectname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###