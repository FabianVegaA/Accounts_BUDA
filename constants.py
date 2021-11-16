from typing import List, Tuple

QUERIES: List[Tuple[str, str]] = [
    (
        "¿Cuánto se ha transado por país de residencia en los últimos 30 días?",
        """
        SELECT residence_country, SUM(monthly_transacted_cents) AS monthly_transacted_cents
        FROM accounts
        GROUP BY residence_country;
        """,
    ),
    (
        "¿Cuánto es lo máximo que ha transado un usuario en los últimos 30 días por cada país de residencia?",
        """
        SELECT id, residence_country, MAX(monthly_transacted_cents) AS max_monthly_transacted_cents
        FROM accounts
        GROUP BY residence_country;
        """,
    ),
    (
        "¿Qué día se crearon la mayor cantidad de cuentas para cada país de residencia?",
        """
        SELECT residence_country, created_at, MAX(amoung) AS max_created_at
        FROM (
            SELECT residence_country, 
                    created_at, 
                    COUNT(created_at) AS amoung
            FROM (
                            SELECT residence_country,
                                    DATE(SUBSTR(created_at, 1, 10)) AS created_at
                            FROM accounts
                    )
            GROUP BY created_at
                )
        GROUP BY residence_country;
        """,
    ),
    (
        "Cantidad porcentual de usuarios inactivos por cada país, entendiendo como usuario inactivo aquel usuario que no tienen monto transado en los últimos 30 días.",
        """
        SELECT residence_country, porcentage
        FROM (
                        SELECT a.residence_country AS residence_country,
                                (COUNT(a.id) * 100 / b.amount) || '%' AS porcentage
                        FROM accounts AS a
                                INNER JOIN (
                                        SELECT residence_country,
                                                COUNT(id) AS amount
                                        FROM accounts
                                        GROUP BY residence_country
                                ) AS b ON b.residence_country = a.residence_country
                        WHERE a.monthly_transacted_cents = 0
                        GROUP BY a.residence_country
                );
        """,
    ),
    (
        "¿Cuántos usuarios con verificación básica o avanzada no han operado en los últimos 30 días?",
        """
        SELECT COUNT(id) AS users
        FROM accounts
        WHERE level_id = 1
                OR level_id = 2
                AND monthly_transacted_cents = 0;
        """,
    ),
]


SELECT_SQL_REGEX = r"\s*SELECT .+\n"
COLS_SELECT_REGEX: str = (
    r"[a-zA-Z0-9_(),.]+ AS ([a-zA-Z0-9_(),.]+),?|([a-zA-Z0-9_(),.]+),?"
)
ALIAS_SQL_REGEX: str = r"\S+? AS (\S+)"
