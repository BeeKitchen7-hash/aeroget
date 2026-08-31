"""
Configuration des data brokers et services de suppression
"""

DATA_BROKERS_CONFIG = {
    'us_brokers': [
        {
            'name': 'PeopleFinder',
            'url': 'https://www.peoplefinder.com',
            'remove_url': 'https://www.peoplefinder.com/opt-out',
            'type': 'people_search',
            'method': 'web_form'
        },
        {
            'name': 'Whitepages',
            'url': 'https://www.whitepages.com',
            'remove_url': 'https://www.whitepages.com/suppression-demande',
            'type': 'people_search',
            'method': 'email'
        },
        {
            'name': 'BeenVerified',
            'url': 'https://www.beenverified.com',
            'remove_url': 'https://www.beenverified.com/app/optout',
            'type': 'background_check',
            'method': 'web_form'
        },
        {
            'name': 'Spokeo',
            'url': 'https://www.spokeo.com',
            'remove_url': 'https://www.spokeo.com/optout',
            'type': 'people_search',
            'method': 'web_form'
        },
        {
            'name': 'MyLife',
            'url': 'https://www.mylife.com',
            'remove_url': 'https://www.mylife.com/privacy-center/opt-out',
            'type': 'background_check',
            'method': 'email'
        },
    ],
    
    'eu_brokers': [
        {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com',
            'remove_url': 'https://www.linkedin.com/psettings/privacy',
            'type': 'professional_network',
            'method': 'account_settings'
        },
        {
            'name': 'Facebook',
            'url': 'https://www.facebook.com',
            'remove_url': 'https://www.facebook.com/privacy',
            'type': 'social_network',
            'method': 'account_settings'
        },
        {
            'name': 'Google',
            'url': 'https://www.google.com',
            'remove_url': 'https://myaccount.google.com/privacy',
            'type': 'search_engine',
            'method': 'account_settings'
        },
    ],
    
    'credit_brokers': [
        {
            'name': 'Equifax',
            'url': 'https://www.equifax.com',
            'remove_url': 'https://www.equifax.com/personal/credit-report-services/credit-freeze/',
            'type': 'credit_bureau',
            'method': 'web_form'
        },
        {
            'name': 'Experian',
            'url': 'https://www.experian.com',
            'remove_url': 'https://www.experian.com/security/freeze-credit',
            'type': 'credit_bureau',
            'method': 'web_form'
        },
        {
            'name': 'Transunion',
            'url': 'https://www.transunion.com',
            'remove_url': 'https://www.transunion.com/credit-freeze',
            'type': 'credit_bureau',
            'method': 'web_form'
        },
    ]
}

# Modèles d'email pour les demandes de suppression
EMAIL_TEMPLATES = {
    'data_removal_request': """
Objet: Demande de suppression de données personnelles (RGPD/CCPA)

Chère équipe de suppression de données,

Je vous demande formellement de supprimer toutes mes données personnelles de vos systèmes selon le droit applicable.

Mes informations:
- Nom: {nom}
- Prénom: {prenom}
- Email: {email}
- Téléphone: {telephone}
- Adresse: {adresse}

Je demande la suppression complète et irréversible de toutes mes données conformément aux droits énoncés dans:
- Le Règlement Général sur la Protection des Données (RGPD) - Article 17
- La California Consumer Privacy Act (CCPA)
- Les lois fédérales sur la protection des données

Veuillez confirmer la suppression complète de mes données dans les 30 jours.

Cordialement,
{prenom} {nom}
    """,
    
    'ccpa_request': """
Objet: Demande d'exercice des droits de confidentialité du consommateur en Californie (CCPA)

Chère équipe de confidentialité,

En tant que résident de Californie, j'exerce mes droits conformément à la California Consumer Privacy Act (CCPA).

Je demande:
1. La suppression de toutes mes données personnelles
2. Une explication de ce qui a été collecté
3. Une confirmation écrite que la suppression est complète

Mes informations personnelles:
- Nom: {nom}
- Prénom: {prenom}
- Email: {email}
- Numéro de téléphone: {telephone}

Veuillez répondre dans les 45 jours.

Cordialement,
{prenom} {nom}
    """,
    
    'gdpr_request': """
Objet: Exercice des droits RGPD - Droit à l'oubli (Article 17)

Madame, Monsieur,

Par la présente, j'exerce mon droit à l'oubli conformément à l'article 17 du RGPD.

Je demande la suppression complète et irréversible de l'ensemble de mes données personnelles stockées chez vous.

Données personnelles concernées:
- Nom: {nom}
- Prénom: {prenom}
- Email: {email}
- Téléphone: {telephone}
- Adresse: {adresse} {code_postal} {ville} {pays}

Cette demande porte sur:
- Tous les profils créés
- Tous les enregistrements
- Tous les fichiers journaux
- Toutes les copies de sauvegarde (sauf obligation légale)

Veuillez confirmer l'exécution de cette demande sous 30 jours.

Cordialement,
{prenom} {nom}
    """
}

# Services de suppression gratuits et payants
REMOVAL_SERVICES = [
    {
        'name': 'DeleteMe',
        'url': 'https://www.deleteme.com',
        'type': 'automated_removal',
        'price': 'paid',
        'coverage': 200
    },
    {
        'name': 'OneRep',
        'url': 'https://onerep.com',
        'type': 'automated_removal',
        'price': 'paid',
        'coverage': 150
    },
    {
        'name': 'Incogni',
        'url': 'https://incogni.com',
        'type': 'automated_removal',
        'price': 'paid',
        'coverage': 200
    },
    {
        'name': 'Mozilla Monitor',
        'url': 'https://monitor.firefox.com',
        'type': 'monitoring',
        'price': 'free',
        'coverage': 'variable'
    }
]
