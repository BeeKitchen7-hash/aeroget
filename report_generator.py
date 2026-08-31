"""
Générateur de rapports et demandes de suppression
Supporte RGPD, CCPA et autres législations
"""

import json
from datetime import datetime
from typing import Dict, List
from brokers_config import EMAIL_TEMPLATES, DATA_BROKERS_CONFIG, REMOVAL_SERVICES

class RemovalRequestGenerator:
    """Génère les demandes de suppression"""
    
    def __init__(self):
        self.requests = []
    
    def generate_gdpr_request(self, personal_info: Dict) -> str:
        """Génère une demande RGPD (Article 17)"""
        return EMAIL_TEMPLATES['gdpr_request'].format(**personal_info)
    
    def generate_ccpa_request(self, personal_info: Dict) -> str:
        """Génère une demande CCPA"""
        return EMAIL_TEMPLATES['ccpa_request'].format(**personal_info)
    
    def generate_generic_request(self, personal_info: Dict) -> str:
        """Génère une demande générique de suppression"""
        return EMAIL_TEMPLATES['data_removal_request'].format(**personal_info)
    
    def generate_for_broker(self, broker_name: str, personal_info: Dict, legislation: str = 'gdpr') -> Dict:
        """Génère une demande pour un broker spécifique"""
        request = {
            'broker': broker_name,
            'date': datetime.now().isoformat(),
            'legislation': legislation,
            'personal_info': personal_info,
            'message': ''
        }
        
        if legislation == 'gdpr':
            request['message'] = self.generate_gdpr_request(personal_info)
        elif legislation == 'ccpa':
            request['message'] = self.generate_ccpa_request(personal_info)
        else:
            request['message'] = self.generate_generic_request(personal_info)
        
        self.requests.append(request)
        return request
    
    def generate_bulk_requests(self, personal_info: Dict, legislation: str = 'gdpr') -> List[Dict]:
        """Génère les demandes pour tous les brokers"""
        all_brokers = []
        
        # Combiner tous les brokers
        for category in DATA_BROKERS_CONFIG.values():
            all_brokers.extend(category)
        
        requests = []
        for broker in all_brokers:
            request = self.generate_for_broker(broker['name'], personal_info, legislation)
            requests.append(request)
        
        return requests
    
    def export_requests_to_file(self, filename: str) -> bool:
        """Exporte les demandes en fichier JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.requests, f, indent=2, ensure_ascii=False)
            return True
        except:
            return False


class ReportGenerator:
    """Génère des rapports d'analyse"""
    
    def __init__(self):
        self.report = {}
    
    def generate_summary_report(self, 
                               personal_info: Dict,
                               system_clean_results: List = None,
                               data_broker_results: List = None,
                               browser_results: List = None) -> Dict:
        """Génère un rapport complet"""
        
        self.report = {
            'title': 'Rapport d\'Analyse Aeroget',
            'date': datetime.now().isoformat(),
            'personal_info': personal_info,
            'summary': {
                'total_threats_found': 0,
                'total_items_cleaned': 0,
                'risk_level': 'Faible',
            },
            'details': {
                'system_cleaning': system_clean_results or [],
                'data_brokers': data_broker_results or [],
                'browsers': browser_results or [],
            },
            'recommendations': self._generate_recommendations(
                system_clean_results,
                data_broker_results,
                browser_results
            )
        }
        
        # Calculer le résumé
        if data_broker_results:
            for result in data_broker_results:
                if 'profiles_found' in result:
                    self.report['summary']['total_threats_found'] += result['profiles_found']
        
        if browser_results:
            for result in browser_results:
                if 'details' in result:
                    for browser_data in result['details'].values():
                        self.report['summary']['total_threats_found'] += browser_data.get('matches_count', 0)
        
        # Déterminer le niveau de risque
        total = self.report['summary']['total_threats_found']
        if total == 0:
            self.report['summary']['risk_level'] = '🟢 Faible'
        elif total < 5:
            self.report['summary']['risk_level'] = '🟡 Moyen'
        elif total < 10:
            self.report['summary']['risk_level'] = '🟠 Élevé'
        else:
            self.report['summary']['risk_level'] = '🔴 Très élevé'
        
        return self.report
    
    def _generate_recommendations(self, 
                                  system_clean: List = None,
                                  data_brokers: List = None,
                                  browsers: List = None) -> List[str]:
        """Génère des recommandations basées sur l'analyse"""
        recommendations = []
        
        recommendations.append("✓ Exécutez régulièrement Aeroget (tous les mois)")
        recommendations.append("✓ Utilisez un gestionnaire de mots de passe")
        recommendations.append("✓ Activez l'authentification à deux facteurs")
        recommendations.append("✓ Vérifiez votre historique de crédit annuellement")
        
        if data_brokers and any(r.get('profiles_found', 0) > 0 for r in data_brokers):
            recommendations.append("🔴 URGENT: Vous avez des profils chez les data brokers - Demandez la suppression immédiatement")
        
        if browsers and any(r.get('details') for r in browsers):
            recommendations.append("🟡 Votre historique navigateur contient vos données personnelles - Nettoyez régulièrement")
        
        recommendations.append("✓ Configurez le mode privé par défaut dans vos navigateurs")
        recommendations.append("✓ Utilisez un VPN pour protéger votre adresse IP")
        recommendations.append("✓ Désactivez les cookies tiers dans vos navigateurs")
        
        return recommendations
    
    def export_to_json(self, filename: str) -> bool:
        """Exporte le rapport en JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.report, f, indent=2, ensure_ascii=False)
            return True
        except:
            return False
    
    def export_to_html(self, filename: str) -> bool:
        """Exporte le rapport en HTML"""
        try:
            html_content = self._generate_html()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            return True
        except:
            return False
    
    def _generate_html(self) -> str:
        """Génère le contenu HTML du rapport"""
        html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.report['title']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #87CEEB 0%, #E0FFFF 100%);
            padding: 20px;
            color: #1E90FF;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            border-bottom: 3px solid #FF8C00;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        h1 {{
            color: #1E90FF;
            font-size: 32px;
            margin: 0;
        }}
        .date {{
            color: #666;
            font-size: 14px;
        }}
        .summary {{
            background: #F0F8FF;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 5px solid {self._get_risk_color()};
        }}
        .risk-level {{
            font-size: 24px;
            font-weight: bold;
            margin: 10px 0;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .section h2 {{
            color: #1E90FF;
            border-bottom: 2px solid #FF8C00;
            padding-bottom: 10px;
        }}
        .item {{
            padding: 10px;
            margin: 10px 0;
            background: #F9F9F9;
            border-left: 4px solid #87CEEB;
            border-radius: 4px;
        }}
        .recommendation {{
            padding: 10px;
            margin: 8px 0;
            background: #FFFACD;
            border-left: 4px solid #FF8C00;
            border-radius: 4px;
        }}
        .personal-info {{
            background: #E0FFFF;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .footer {{
            text-align: center;
            color: #666;
            font-size: 12px;
            margin-top: 40px;
            border-top: 1px solid #CCC;
            padding-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>✨ {self.report['title']} ✨</h1>
            <div class="date">Généré le: {self.report['date']}</div>
        </div>
        
        <div class="summary">
            <h3>📊 Résumé</h3>
            <p><strong>Menaces trouvées:</strong> {self.report['summary']['total_threats_found']}</p>
            <div class="risk-level">Niveau de risque: {self.report['summary']['risk_level']}</div>
        </div>
        
        <div class="section">
            <h2>👤 Informations Personnelles Analysées</h2>
            <div class="personal-info">
                {self._generate_personal_info_html()}
            </div>
        </div>
        
        <div class="section">
            <h2>🧹 Nettoyage Système</h2>
            {self._generate_system_clean_html()}
        </div>
        
        <div class="section">
            <h2>🔍 Données Personnelles</h2>
            {self._generate_data_brokers_html()}
        </div>
        
        <div class="section">
            <h2>🌐 Navigateurs</h2>
            {self._generate_browsers_html()}
        </div>
        
        <div class="section">
            <h2>💡 Recommandations</h2>
            {self._generate_recommendations_html()}
        </div>
        
        <div class="footer">
            <p>Aeroget - Nettoyeur de Données Personnelles | Style Frutiger Aero</p>
            <p>© 2024 BeeKitchen7-hash | <a href="https://github.com/BeeKitchen7-hash/aeroget">GitHub</a></p>
        </div>
    </div>
</body>
</html>
        """
        return html
    
    def _get_risk_color(self) -> str:
        """Retourne la couleur du risque"""
        risk_level = self.report['summary']['risk_level']
        if 'Faible' in risk_level:
            return '#00FF00'
        elif 'Moyen' in risk_level:
            return '#FFD700'
        elif 'Élevé' in risk_level:
            return '#FF8C00'
        else:
            return '#FF0000'
    
    def _generate_personal_info_html(self) -> str:
        """Génère le HTML des infos personnelles"""
        html = ""
        for key, value in self.report['personal_info'].items():
            if value:
                html += f"<p><strong>{key.replace('_', ' ').capitalize()}:</strong> {value}</p>"
        return html
    
    def _generate_system_clean_html(self) -> str:
        """Génère le HTML du nettoyage système"""
        html = ""
        for item in self.report['details']['system_cleaning']:
            html += f"""
            <div class="item">
                <strong>{item.get('action', '')}</strong>
                <p>{item.get('status', '')}</p>
            </div>
            """
        return html or "<p>Aucun résultat</p>"
    
    def _generate_data_brokers_html(self) -> str:
        """Génère le HTML des data brokers"""
        html = ""
        for item in self.report['details']['data_brokers']:
            html += f"""
            <div class="item">
                <strong>{item.get('action', '')}</strong>
                <p>{item.get('status', '')}</p>
            </div>
            """
        return html or "<p>Aucun résultat</p>"
    
    def _generate_browsers_html(self) -> str:
        """Génère le HTML des navigateurs"""
        html = ""
        for item in self.report['details']['browsers']:
            html += f"""
            <div class="item">
                <strong>{item.get('action', '')}</strong>
                <p>{item.get('status', '')}</p>
            </div>
            """
        return html or "<p>Aucun résultat</p>"
    
    def _generate_recommendations_html(self) -> str:
        """Génère le HTML des recommandations"""
        html = ""
        for rec in self.report['recommendations']:
            html += f'<div class="recommendation">{rec}</div>'
        return html
