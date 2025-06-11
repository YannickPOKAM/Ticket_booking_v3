event_manager/
│
├── app/
│   ├── __init__.py              # Initialisation de l'app Flask
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py       # Routes d'inscription/connexion
│   │   ├── user_routes.py       # Tableau de bord utilisateur, réservation
│   │   ├── admin_routes.py      # Gestion des événements et réservations
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── booking.py
│   ├── templates/               # Tes fichiers HTML déjà prêts
│   ├── static/                  # Ton CSS déjà prêt
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth.py              # JWT, bcrypt
│   │   ├── decorators.py        # Vérification des rôles (admin, user)
│   └── config.py                # Configurations Flask + DB
│
├── database/
│   ├── init_db.py               # Script de création de la BD (ORM ou SQL brut)
│
├── .env                         # Variables d’environnement
├── run.py                       # Point d’entrée Flask
├── requirements.txt             # Librairies nécessaires
└── README.md