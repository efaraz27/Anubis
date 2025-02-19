"""ADD hide_due_date

Revision ID: fff88033d4f9
Revises: a242e0e21f3e
Create Date: 2021-08-24 23:35:54.420050

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "fff88033d4f9"
down_revision = "a242e0e21f3e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("assignment", sa.Column("hide_due_date", sa.Boolean(), nullable=True))
    op.alter_column(
        "assignment_repo",
        "repo_url",
        existing_type=mysql.VARCHAR(collation="utf8mb4_unicode_ci", length=512),
        nullable=False,
    )
    conn = op.get_bind()
    with conn.begin():
        conn.execute("update assignment set hide_due_date = 0;")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "assignment_repo",
        "repo_url",
        existing_type=mysql.VARCHAR(collation="utf8mb4_unicode_ci", length=512),
        nullable=True,
    )
    op.drop_column("assignment", "hide_due_date")
    # ### end Alembic commands ###
