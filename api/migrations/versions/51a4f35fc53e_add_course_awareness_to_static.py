"""ADD course awareness to static

Revision ID: 51a4f35fc53e
Revises: 452a7485f568
Create Date: 2021-04-27 21:37:27.563873

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "51a4f35fc53e"
down_revision = "452a7485f568"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    with conn.begin():
        op.add_column(
            "static_file",
            sa.Column("course_id", sa.String(length=128)),
        )
        op.create_index(
            op.f("ix_static_file_course_id"),
            "static_file",
            ["course_id"],
            unique=False,
        )
        op.add_column(
            "theia_session",
            sa.Column("course_id", sa.String(length=128)),
        )
        op.create_index(
            op.f("ix_theia_session_course_id"),
            "theia_session",
            ["course_id"],
            unique=False,
        )
        op.create_foreign_key(None, "static_file", "course", ["course_id"], ["id"])
        op.create_foreign_key(None, "theia_session", "course", ["course_id"], ["id"])

        try:
            (course_id,) = conn.execute(
                "select id from course where course_code = 'CS-UY 3224';"
            ).fetchone()
            conn.execute("update static_file set course_id = %s;", (course_id,))
            conn.execute("update theia_session set course_id = %s;", (course_id,))

            op.alter_column(
                "static_file", "course_id", existing_type=sa.String(128), nullable=False
            )
            op.alter_column(
                "theia_session",
                "course_id",
                existing_type=sa.String(128),
                nullable=False,
            )
        except TypeError:
            pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "static_file", type_="foreignkey")
    op.drop_index(op.f("ix_static_file_course_id"), table_name="static_file")

    op.drop_constraint(None, "theia_session", type_="foreignkey")
    op.drop_index(op.f("ix_theia_session_course_id"), table_name="theia_session")

    op.drop_column("static_file", "course_id")
    op.drop_column("theia_session", "course_id")
    # ### end Alembic commands ###
