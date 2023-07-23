"""create an address table

Revision ID: d9dc79f9b185
Revises: 
Create Date: 2023-07-23 17:23:45.908631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9dc79f9b185'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id',sa.Integer, primary_key=True),
                    sa.Column('address',sa.String(50), nullable = False), 
                    sa.Column('city', sa.String(50), nullable = False), 
                    sa.Column('state', sa.String(50), nullable = False))


def downgrade():
    op.drop_table('address')
