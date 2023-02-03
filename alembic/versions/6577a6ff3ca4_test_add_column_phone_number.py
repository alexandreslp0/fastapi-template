"""test add column phone number

Revision ID: 6577a6ff3ca4
Revises: 2d4b93734474
Create Date: 2023-02-03 15:17:31.544198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6577a6ff3ca4'
down_revision = '2d4b93734474'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
