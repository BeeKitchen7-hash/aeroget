"""
Interface graphique Frutiger Aero pour Aeroget
Style années 2000 avec couleurs brillantes et effets Aero
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QTabWidget, QTableWidget,
    QTableWidgetItem, QFileDialog, QMessageBox, QProgressBar, QScrollArea
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QRect
from PyQt6.QtGui import QFont, QColor, QIcon, QPainter, QBrush, QPen, QLinearGradient
from PyQt6.QtCore import QSize

from config import COLORS, FONTS, UI_SETTINGS
from system_cleaner import SystemCleaner
from data_broker_remover import DataBrokerRemover, WebDataSearcher
from browser_analyzer import BrowserAnalyzer

class AeroStyle:
    """Classe pour appliquer le style Frutiger Aero"""
    
    @staticmethod
    def get_stylesheet() -> str:
        """Retourne le CSS Frutiger Aero"""
        return f"""
        QMainWindow {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {COLORS['sky_blue']}, 
                stop:1 {COLORS['gradient_end']});
        }}
        
        QWidget {{
            background: transparent;
        }}
        
        QPushButton {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['orange_gradient']},
                stop:1 {COLORS['orange']});
            color: white;
            border: 2px solid {COLORS['dark_blue']};
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: bold;
            font-size: 11px;
        }}
        
        QPushButton:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['light_purple']},
                stop:1 {COLORS['dark_blue']});
        }}
        
        QPushButton:pressed {{
            padding: 10px 14px;
        }}
        
        QLineEdit {{
            background-color: white;
            border: 2px solid {COLORS['dark_blue']};
            border-radius: 6px;
            padding: 6px;
            font-size: 11px;
        }}
        
        QLineEdit:focus {{
            border: 3px solid {COLORS['orange']};
        }}
        
        QTextEdit {{
            background-color: white;
            border: 2px solid {COLORS['dark_blue']};
            border-radius: 6px;
            padding: 6px;
            font-size: 10px;
        }}
        
        QLabel {{
            color: {COLORS['dark_blue']};
            font-weight: bold;
        }}
        
        QTabWidget {{
            border: 2px solid {COLORS['dark_blue']};
            border-radius: 6px;
        }}
        
        QTabBar::tab {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['silver']},
                stop:1 {COLORS['light_purple']});
            border: 1px solid {COLORS['dark_blue']};
            padding: 6px 20px;
            margin-right: 2px;
            border-radius: 4px 4px 0px 0px;
        }}
        
        QTabBar::tab:selected {{
            background: {COLORS['sky_blue']};
        }}
        
        QProgressBar {{
            border: 2px solid {COLORS['dark_blue']};
            border-radius: 6px;
            text-align: center;
            background-color: white;
        }}
        
        QProgressBar::chunk {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {COLORS['lime']},
                stop:1 {COLORS['orange_gradient']});
            border-radius: 4px;
        }}
        
        QTableWidget {{
            background-color: white;
            border: 2px solid {COLORS['dark_blue']};
            border-radius: 6px;
            gridline-color: {COLORS['light_purple']};
        }}
        
        QTableWidget::item {{
            padding: 4px;
        }}
        
        QHeaderView::section {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {COLORS['sky_blue']},
                stop:1 {COLORS['dark_blue']});
            color: white;
            padding: 5px;
            border: none;
            font-weight: bold;
        }}
        """
    
    @staticmethod
    def create_gradient_button(text: str) -> QPushButton:
        """Crée un bouton avec gradient"""
        button = QPushButton(text)
        button.setFont(QFont(*FONTS['header']))
        return button


class DataInputDialog(QWidget):
    """Dialogue pour saisir les données personnelles"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.personal_info = {}
        self.init_ui()
    
    def init_ui(self):
        """Initialise l'interface"""
        layout = QVBoxLayout()
        
        title = QLabel("🔐 Informations Personnelles")
        title.setFont(QFont(*FONTS['header']))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Créer les champs de saisie
        fields = [
            ('nom', 'Nom:'),
            ('prenom', 'Prénom:'),
            ('email', 'Email:'),
            ('telephone', 'Numéro de téléphone:'),
            ('adresse', 'Adresse:'),
            ('ville', 'Ville:'),
            ('code_postal', 'Code postal:'),
            ('pays', 'Pays:'),
        ]
        
        self.inputs = {}
        for key, label in fields:
            label_widget = QLabel(label)
            label_widget.setFont(QFont(*FONTS['normal']))
            layout.addWidget(label_widget)
            
            input_widget = QLineEdit()
            input_widget.setFont(QFont(*FONTS['normal']))
            self.inputs[key] = input_widget
            layout.addWidget(input_widget)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def get_info(self) -> dict:
        """Retourne les informations saisies"""
        return {key: input_widget.text() for key, input_widget in self.inputs.items()}
    
    def set_info(self, info: dict):
        """Définit les informations"""
        for key, value in info.items():
            if key in self.inputs:
                self.inputs[key].setText(value)


class CleaningThread(QThread):
    """Thread pour exécuter les tâches de nettoyage"""
    
    progress_update = pyqtSignal(str)
    results_ready = pyqtSignal(list)
    
    def __init__(self, task_type: str, personal_info: dict = None):
        super().__init__()
        self.task_type = task_type
        self.personal_info = personal_info or {}
    
    def run(self):
        """Exécute la tâche"""
        if self.task_type == 'system_clean':
            self._system_clean()
        elif self.task_type == 'data_search':
            self._data_search()
        elif self.task_type == 'browser_analysis':
            self._browser_analysis()
    
    def _system_clean(self):
        """Nettoie le système"""
        cleaner = SystemCleaner()
        
        self.progress_update.emit("🗑️ Vidage de la corbeille...")
        cleaner.clean_recycle_bin()
        
        self.progress_update.emit("🧹 Suppression des fichiers temporaires...")
        cleaner.clean_temp_files()
        
        self.progress_update.emit("🌐 Nettoyage des caches navigateurs...")
        cleaner.clean_browser_cache()
        
        self.results_ready.emit(cleaner.get_results())
    
    def _data_search(self):
        """Recherche les données personnelles"""
        broker_remover = DataBrokerRemover()
        web_searcher = WebDataSearcher()
        
        self.progress_update.emit("🔍 Recherche dans les data brokers...")
        broker_remover.search_personal_data(self.personal_info)
        
        self.progress_update.emit("🕷️ Recherche sur le web...")
        web_searcher.search_on_web(self.personal_info)
        
        results = broker_remover.get_results() + web_searcher.get_results()
        self.results_ready.emit(results)
    
    def _browser_analysis(self):
        """Analyse les navigateurs"""
        analyzer = BrowserAnalyzer()
        
        self.progress_update.emit("📊 Analyse des navigateurs...")
        analyzer.analyze_all_browsers(self.personal_info)
        
        self.results_ready.emit(analyzer.get_results())


class AerogetMainWindow(QMainWindow):
    """Fenêtre principale d'Aeroget"""
    
    def __init__(self):
        super().__init__()
        self.personal_info = {}
        self.setWindowTitle("Aeroget - Nettoyeur de Données Frutiger Aero 🌟")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet(AeroStyle.get_stylesheet())
        
        # Icône (emoji)
        self.setWindowIcon(QIcon())
        
        self.init_ui()
    
    def init_ui(self):
        """Initialise l'interface"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout()
        
        # En-tête
        header = self._create_header()
        main_layout.addWidget(header)
        
        # Onglets
        tabs = QTabWidget()
        
        # Onglet 1: Infos personnelles
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("Step 1️⃣: Saisissez vos informations personnelles"))
        self.data_input = DataInputDialog()
        scroll1 = QScrollArea()
        scroll1.setWidget(self.data_input)
        scroll1.setWidgetResizable(True)
        tab1_layout.addWidget(scroll1)
        
        save_btn = AeroStyle.create_gradient_button("💾 Enregistrer les informations")
        save_btn.clicked.connect(self._save_personal_info)
        tab1_layout.addWidget(save_btn)
        tab1.setLayout(tab1_layout)
        tabs.addTab(tab1, "📋 Informations")
        
        # Onglet 2: Nettoyage système
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Step 2️⃣: Nettoyage du système"))
        
        clean_btn = AeroStyle.create_gradient_button("🧹 Nettoyer le système")
        clean_btn.clicked.connect(self._start_system_clean)
        tab2_layout.addWidget(clean_btn)
        
        tab2_layout.addWidget(QLabel("Résultats du nettoyage:"))
        self.clean_results_table = QTableWidget()
        self.clean_results_table.setColumnCount(2)
        self.clean_results_table.setHorizontalHeaderLabels(["Action", "Résultat"])
        tab2_layout.addWidget(self.clean_results_table)
        
        self.clean_progress = QProgressBar()
        tab2_layout.addWidget(self.clean_progress)
        
        tab2.setLayout(tab2_layout)
        tabs.addTab(tab2, "🧹 Nettoyage Système")
        
        # Onglet 3: Recherche données
        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("Step 3️⃣: Recherche des données personnelles"))
        
        search_btn = AeroStyle.create_gradient_button("🔍 Rechercher mes données")
        search_btn.clicked.connect(self._start_data_search)
        tab3_layout.addWidget(search_btn)
        
        tab3_layout.addWidget(QLabel("Données trouvées:"))
        self.data_results_table = QTableWidget()
        self.data_results_table.setColumnCount(3)
        self.data_results_table.setHorizontalHeaderLabels(["Source", "Détails", "Action"])
        tab3_layout.addWidget(self.data_results_table)
        
        self.data_progress = QProgressBar()
        tab3_layout.addWidget(self.data_progress)
        
        tab3.setLayout(tab3_layout)
        tabs.addTab(tab3, "🔍 Données Personnelles")
        
        # Onglet 4: Analyse navigateurs
        tab4 = QWidget()
        tab4_layout = QVBoxLayout()
        tab4_layout.addWidget(QLabel("Step 4️⃣: Analyse des navigateurs"))
        
        browser_btn = AeroStyle.create_gradient_button("🌐 Analyser les navigateurs")
        browser_btn.clicked.connect(self._start_browser_analysis)
        tab4_layout.addWidget(browser_btn)
        
        tab4_layout.addWidget(QLabel("Données trouvées sur les navigateurs:"))
        self.browser_results_table = QTableWidget()
        self.browser_results_table.setColumnCount(3)
        self.browser_results_table.setHorizontalHeaderLabels(["Navigateur", "Informations", "Nombre"])
        tab4_layout.addWidget(self.browser_results_table)
        
        self.browser_progress = QProgressBar()
        tab4_layout.addWidget(self.browser_progress)
        
        tab4.setLayout(tab4_layout)
        tabs.addTab(tab4, "🌐 Navigateurs")
        
        main_layout.addWidget(tabs)
        
        # Pied de page
        footer = self._create_footer()
        main_layout.addWidget(footer)
        
        main_widget.setLayout(main_layout)
    
    def _create_header(self) -> QWidget:
        """Crée l'en-tête"""
        header = QWidget()
        header_layout = QVBoxLayout()
        
        title = QLabel("✨ Aeroget - Nettoyeur de Données Personnelles ✨")
        title.setFont(QFont(*FONTS['title']))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {COLORS['dark_blue']}; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);")
        
        subtitle = QLabel("Nettoyez votre corbeille, supprimez les fichiers temporaires et maîtrisez vos données personnelles")
        subtitle.setFont(QFont(*FONTS['normal']))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet(f"color: {COLORS['dark_blue']};")
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        header.setLayout(header_layout)
        
        return header
    
    def _create_footer(self) -> QWidget:
        """Crée le pied de page"""
        footer = QWidget()
        footer_layout = QHBoxLayout()
        
        status_label = QLabel("✓ Prêt à nettoyer vos données!")
        status_label.setFont(QFont(*FONTS['small']))
        status_label.setStyleSheet(f"color: {COLORS['dark_blue']};")
        
        export_btn = AeroStyle.create_gradient_button("📊 Exporter le rapport")
        export_btn.clicked.connect(self._export_report)
        
        footer_layout.addWidget(status_label)
        footer_layout.addStretch()
        footer_layout.addWidget(export_btn)
        
        footer.setLayout(footer_layout)
        return footer
    
    def _save_personal_info(self):
        """Enregistre les informations personnelles"""
        self.personal_info = self.data_input.get_info()
        QMessageBox.information(self, "✓ Succès", "Informations enregistrées avec succès!")
    
    def _start_system_clean(self):
        """Démarre le nettoyage du système"""
        self.clean_progress.setValue(0)
        self.thread = CleaningThread('system_clean')
        self.thread.progress_update.connect(self._update_clean_status)
        self.thread.results_ready.connect(self._display_clean_results)
        self.thread.start()
    
    def _start_data_search(self):
        """Démarre la recherche de données"""
        if not self.personal_info:
            QMessageBox.warning(self, "⚠️ Attention", "Veuillez d'abord saisir vos informations!")
            return
        
        self.data_progress.setValue(0)
        self.thread = CleaningThread('data_search', self.personal_info)
        self.thread.progress_update.connect(self._update_data_status)
        self.thread.results_ready.connect(self._display_data_results)
        self.thread.start()
    
    def _start_browser_analysis(self):
        """Démarre l'analyse des navigateurs"""
        if not self.personal_info:
            QMessageBox.warning(self, "⚠️ Attention", "Veuillez d'abord saisir vos informations!")
            return
        
        self.browser_progress.setValue(0)
        self.thread = CleaningThread('browser_analysis', self.personal_info)
        self.thread.progress_update.connect(self._update_browser_status)
        self.thread.results_ready.connect(self._display_browser_results)
        self.thread.start()
    
    def _update_clean_status(self, message: str):
        """Met à jour le statut du nettoyage"""
        self.statusBar().showMessage(message)
        self.clean_progress.setValue(min(self.clean_progress.value() + 30, 90))
    
    def _update_data_status(self, message: str):
        """Met à jour le statut de la recherche"""
        self.statusBar().showMessage(message)
        self.data_progress.setValue(min(self.data_progress.value() + 25, 90))
    
    def _update_browser_status(self, message: str):
        """Met à jour le statut de l'analyse"""
        self.statusBar().showMessage(message)
        self.browser_progress.setValue(min(self.browser_progress.value() + 20, 90))
    
    def _display_clean_results(self, results: list):
        """Affiche les résultats du nettoyage"""
        self.clean_results_table.setRowCount(len(results))
        for row, result in enumerate(results):
            self.clean_results_table.setItem(row, 0, QTableWidgetItem(result.get('action', '')))
            self.clean_results_table.setItem(row, 1, QTableWidgetItem(result.get('status', '')))
        
        self.clean_progress.setValue(100)
        self.statusBar().showMessage("✓ Nettoyage du système terminé!")
    
    def _display_data_results(self, results: list):
        """Affiche les résultats de la recherche de données"""
        self.data_results_table.setRowCount(len(results))
        for row, result in enumerate(results):
            self.data_results_table.setItem(row, 0, QTableWidgetItem(result.get('action', '')))
            self.data_results_table.setItem(row, 1, QTableWidgetItem(result.get('status', '')))
            
            # Bouton de suppression
            remove_btn = AeroStyle.create_gradient_button("🗑️ Supprimer")
            self.data_results_table.setCellWidget(row, 2, remove_btn)
        
        self.data_progress.setValue(100)
        self.statusBar().showMessage("✓ Recherche de données terminée!")
    
    def _display_browser_results(self, results: list):
        """Affiche les résultats de l'analyse navigateurs"""
        self.browser_results_table.setRowCount(len(results))
        for row, result in enumerate(results):
            if 'details' in result and result['details']:
                for browser_name, browser_data in result['details'].items():
                    browser_row = self.browser_results_table.rowCount()
                    self.browser_results_table.insertRow(browser_row)
                    self.browser_results_table.setItem(browser_row, 0, QTableWidgetItem(browser_name))
                    self.browser_results_table.setItem(browser_row, 1, QTableWidgetItem(
                        f"Historique: {len(browser_data.get('history', []))} | Cookies: {len(browser_data.get('cookies', []))}"
                    ))
                    self.browser_results_table.setItem(browser_row, 2, QTableWidgetItem(
                        str(browser_data.get('matches_count', 0))
                    ))
        
        self.browser_progress.setValue(100)
        self.statusBar().showMessage("✓ Analyse des navigateurs terminée!")
    
    def _export_report(self):
        """Exporte un rapport"""
        filepath, _ = QFileDialog.getSaveFileName(self, "Exporter le rapport", "", "JSON Files (*.json)")
        if filepath:
            import json
            report = {
                'personal_info': self.personal_info,
                'clean_results': self._get_table_data(self.clean_results_table),
                'data_results': self._get_table_data(self.data_results_table),
                'browser_results': self._get_table_data(self.browser_results_table),
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            QMessageBox.information(self, "✓ Succès", f"Rapport exporté vers {filepath}")
    
    def _get_table_data(self, table: QTableWidget) -> list:
        """Récupère les données d'un tableau"""
        data = []
        for row in range(table.rowCount()):
            row_data = {}
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    row_data[f"col_{col}"] = item.text()
            if row_data:
                data.append(row_data)
        return data


def main():
    """Fonction principale"""
    app = QApplication(sys.argv)
    window = AerogetMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
