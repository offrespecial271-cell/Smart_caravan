# SMART CARAVAN FCM READY
# -*- coding: utf-8 -*-
# SMART CARAVAN - Kivy Android
# Version: 4.4 FINAL - validated source / leadership edition / no login
#
# Run:
#   pip install kivy
# then run this file in Pydroid 3.
#
# Direct-open version: no username/password required.

import os
import json
import copy
from datetime import datetime
import threading
import time
import urllib.request
import urllib.parse

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox


# ============================================================
# COLOURS
# ============================================================

BG       = (0.965, 0.975, 0.99, 1)
WHITE    = (1, 1, 1, 1)
NAVY     = (0.055, 0.105, 0.19, 1)
TEXT     = (0.10, 0.13, 0.19, 1)
MUTED    = (0.42, 0.46, 0.53, 1)

BLUE     = (0.08, 0.43, 0.88, 1)
CYAN     = (0.02, 0.67, 0.78, 1)
GREEN    = (0.08, 0.66, 0.39, 1)
RED      = (0.90, 0.19, 0.23, 1)
ORANGE   = (0.97, 0.57, 0.10, 1)
PURPLE   = (0.53, 0.31, 0.84, 1)
TEAL     = (0.02, 0.57, 0.52, 1)
PINK     = (0.88, 0.26, 0.52, 1)
LIGHTBLUE= (0.90, 0.95, 1.00, 1)
LIGHTRED = (1.00, 0.93, 0.94, 1)
LIGHTGREEN=(0.91, 0.98, 0.94, 1)
LIGHTORANGE=(1.00, 0.96, 0.89, 1)
LIGHTPURPLE=(0.96, 0.93, 1.00, 1)

Window.clearcolor = BG
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "smart_caravan_logo.png")

# The logo is also embedded so the app can display it even if the PNG was
# not copied beside the Python file.
EMBEDDED_LOGO_B64 = "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAADwf7zUAABbs0lEQVR4nO3dd5xddZ0//nNn7vSW3nslCSEhoXeQJshawS6uYmMtX93V1V0LWFC/qz93dVVUVERXFJXFgggC0nuAkEBCCqmQXmcm02d+f4QvQjJzp917z73383w+5rGPZcr5fI4n95z363w+53MS5WMXRgAAQBiK4u4AAACQPQIAAAAERAAAAICACAAAABAQAQAAAAIiAAAAQEAEAAAACIgAAAAAAREAAAAgIAIAAAAERAAAAICACAAAABAQAQAAAAIiAAAAQECSUZSIuw8AAECWGAEAAICACAAAABAQAQAAAAIiAAAAQEAEAAAACIgAAAAAAREAAAAgIAIAAAAERAAAAICACAAAABCQZJSIuwsAAEC2GAEAAICACAAAABAQAQAAAAKSjDwEAAAAwTACAAAAAREAAAAgIAIAAAAERAAAAICACAAAABAQAQAAAAIiAAAAQEAEAAAACIgAAAAAAREAAAAgIAIAAAAERAAAAICACAAAABCQZBQl4u4DAACQJUYAAAAgIAIAAAAERAAAAICACAAAABAQAQAAAAIiAAAAQEAEAAAACEjSawAAACAcRgAAACAgAgAAAAREAAAAgIAIAAAAEBABAAAAAiIAAABAQJKRdUABACAYRgAAACAgAgAAAAREAAAAgIAIAAAAEBABAAAAAiIAAABAQAQAAAAIiAAAAAABEQAAACAgAgAAAAREAAAAgIAIAAAAEBABAAAAAiIAAABAQJJRlIi7DwAAQJYYAQAAgIAIAAAAEJCkGUAAABAOIwAAABAQAQAAAAIiAAAAQEAEAAAACIgAAAAAAREAAAAgIAIAAAAERAAAAICACAAAABAQAQAAAAKSjKJE3H0AAACyxAgAAAAERAAAAICACAAAABAQAQAAAAIiAAAAQEAEAAAACIgAAAAAAREAAAAgIAIAAAAERAAAAICACAAAABAQAQAAAAIiAAAAQEAEAAAACEgykUjE3QcAACBLjAAAAEBABAAAAAiIAAAAAAERAAAAICACAAAABEQAAACAgAgAAAAQEAEAAAACIgAAAEBABAAAAAiIAAAAAAERAAAAICACAAAABEQAAACAgCSjKBF3HwAAgCwxAgAAAAERAAAAICACAAAABEQAAACAgAgAAAAQEAEAAAACIgAA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"

def ensure_logo():
    if os.path.exists(LOGO_PATH):
        return LOGO_PATH
    if not EMBEDDED_LOGO_B64:
        return ""
    try:
        out = os.path.join(App.get_running_app().user_data_dir, "smart_caravan_logo.png")
        if not os.path.exists(out):
            import base64 as _b64
            with open(out, "wb") as f:
                f.write(_b64.b64decode(EMBEDDED_LOGO_B64))
        return out
    except Exception:
        return ""


# ============================================================
# ARABIC FONT
# ============================================================

AR_FONT = None
for fp in (
    "/system/fonts/NotoNaskhArabic-Regular.ttf",
    "/system/fonts/NotoSansArabic-Regular.ttf",
    "/system/fonts/NotoSansArabicUI-Regular.ttf",
    "/system/fonts/DroidSansArabic.ttf",
):
    if os.path.exists(fp):
        AR_FONT = fp
        break

if AR_FONT:
    try:
        LabelBase.register(name="SCArabic", fn_regular=AR_FONT)
    except Exception:
        pass


def current_font(lang):
    if lang == "ar" and AR_FONT:
        return "SCArabic"
    return "Roboto"


# ============================================================
# TRANSLATIONS
# ============================================================

T = {
"fr": {
"title":"SMART CARAVAN",
"subtitle":"Gestion intelligente de la caravane",
"login":"Connexion",
"username":"Nom d'utilisateur",
"password":"Mot de passe",
"connect":"Se connecter",
"dashboard":"Tableau de bord",
"welcome":"Bienvenue",
"danger":"Signaler un danger",
"participants":"Participants",
"health":"Caravane sanitaire",
"notifications":"Notifications",
"reports":"Rapports",
"settings":"Parametres",
"logout":"Deconnexion",
"back":"Retour",
"quick":"Acces rapide",
"recent":"Signalements recents",
"total":"Total",
"open":"Ouverts",
"critical":"Critiques",
"members":"Membres",
"name":"Nom",
"phone":"Telephone",
"location":"Lieu",
"description":"Description",
"danger_type":"Type de danger",
"priority":"Priorite",
"send":"Envoyer le signalement",
"add":"Ajouter",
"save":"Enregistrer",
"delete":"Supprimer",
"resolve":"Resoudre",
"no_data":"Aucune donnee.",
"language":"Langue",
"server":"Serveur API",
"server_hint":"https://votre-serveur.tn/api",
"health_status":"Etat sanitaire",
"ambulance":"Ambulance",
"available":"Disponible",
"busy":"Occupee",
"good":"Bon",
"watch":"A surveiller",
"emergency":"Urgence",
"accident":"Accident",
"fire":"Incendie",
"security":"Securite",
"medical":"Urgence medicale",
"vehicle":"Panne de vehicule",
"road":"Probleme routier",
"crowd":"Foule / mouvement",
"other":"Autre",
"low":"Faible",
"medium":"Moyenne",
"high":"Elevee",
"critical":"Critique",
"saved":"Enregistre avec succes.",
"required":"Veuillez remplir les champs obligatoires.",
"wrong":"Identifiants incorrects.",
"admin":"Administrateur",
"leader":"Coordinateur",
"member":"Participant",
"demo":"Test: admin / leader / member — mot de passe: 1234",
"local":"Donnees locales",
"sync":"Synchronisation",
"not_connected":"Serveur non configure",
"about":"Smart Caravan permet a l'equipe de suivre la caravane, signaler les risques et centraliser les informations.",
"app_version":"Version 1.0",
"clear":"Effacer les notifications",
"yes":"Oui",
"cancel":"Annuler",
"notification_new":"Nouveau signalement",
"status":"Statut",
"date":"Date"
},
"en": {
"title":"SMART CARAVAN",
"subtitle":"Smart caravan management",
"login":"Login",
"username":"Username",
"password":"Password",
"connect":"Sign in",
"dashboard":"Dashboard",
"welcome":"Welcome",
"danger":"Report a danger",
"participants":"Participants",
"health":"Health caravan",
"notifications":"Notifications",
"reports":"Reports",
"settings":"Settings",
"logout":"Logout",
"back":"Back",
"quick":"Quick access",
"recent":"Recent reports",
"total":"Total",
"open":"Open",
"critical":"Critical",
"members":"Members",
"name":"Name",
"phone":"Phone",
"location":"Location",
"description":"Description",
"danger_type":"Danger type",
"priority":"Priority",
"send":"Send report",
"add":"Add",
"save":"Save",
"delete":"Delete",
"resolve":"Resolve",
"no_data":"No data.",
"language":"Language",
"server":"API server",
"server_hint":"https://your-server.tn/api",
"health_status":"Health status",
"ambulance":"Ambulance",
"available":"Available",
"busy":"Busy",
"good":"Good",
"watch":"Needs attention",
"emergency":"Emergency",
"accident":"Accident",
"fire":"Fire",
"security":"Security",
"medical":"Medical emergency",
"vehicle":"Vehicle breakdown",
"road":"Road problem",
"crowd":"Crowd / movement",
"other":"Other",
"low":"Low",
"medium":"Medium",
"high":"High",
"critical":"Critical",
"saved":"Saved successfully.",
"required":"Please fill the required fields.",
"wrong":"Incorrect username or password.",
"admin":"Administrator",
"leader":"Coordinator",
"member":"Participant",
"demo":"Test: admin / leader / member — password: 1234",
"local":"Local data",
"sync":"Synchronisation",
"not_connected":"Server not configured",
"about":"Smart Caravan helps the team monitor the caravan, report risks and centralise information.",
"app_version":"Version 1.0",
"clear":"Clear notifications",
"yes":"Yes",
"cancel":"Cancel",
"notification_new":"New report",
"status":"Status",
"date":"Date"
},
"ar": {
"title":"القافلة الذكية",
"subtitle":"الإدارة الذكية للقافلة",
"login":"تسجيل الدخول",
"username":"اسم المستخدم",
"password":"كلمة المرور",
"connect":"دخول",
"dashboard":"لوحة التحكم",
"welcome":"مرحبا",
"danger":"الإبلاغ عن خطر",
"participants":"المشاركون",
"health":"القافلة الصحية",
"notifications":"الإشعارات",
"reports":"التقارير",
"settings":"الإعدادات",
"logout":"تسجيل الخروج",
"back":"رجوع",
"quick":"الوصول السريع",
"recent":"آخر البلاغات",
"total":"المجموع",
"open":"المفتوحة",
"critical":"الحرجة",
"members":"المشاركون",
"name":"الاسم",
"phone":"الهاتف",
"location":"المكان",
"description":"الوصف",
"danger_type":"نوع الخطر",
"priority":"الأولوية",
"send":"إرسال البلاغ",
"add":"إضافة",
"save":"حفظ",
"delete":"حذف",
"resolve":"حل البلاغ",
"no_data":"لا توجد بيانات.",
"language":"اللغة",
"server":"خادم API",
"server_hint":"https://your-server.tn/api",
"health_status":"الحالة الصحية",
"ambulance":"سيارة الإسعاف",
"available":"متاحة",
"busy":"مشغولة",
"good":"جيدة",
"watch":"تحتاج متابعة",
"emergency":"طارئة",
"accident":"حادث",
"fire":"حريق",
"security":"خطر أمني",
"medical":"حالة صحية طارئة",
"vehicle":"عطب في سيارة",
"road":"مشكلة في الطريق",
"crowd":"ازدحام / حركة",
"other":"خطر آخر",
"low":"منخفضة",
"medium":"متوسطة",
"high":"مرتفعة",
"critical":"حرجة",
"saved":"تم الحفظ بنجاح.",
"required":"يرجى ملء الخانات المطلوبة.",
"wrong":"اسم المستخدم أو كلمة المرور غير صحيحة.",
"admin":"مسؤول",
"leader":"منسق",
"member":"مشارك",
"demo":"للتجربة: admin / leader / member — كلمة السر: 1234",
"local":"بيانات محلية",
"sync":"المزامنة",
"not_connected":"الخادم غير مضبوط",
"about":"Smart Caravan تساعد الفريق على متابعة القافلة والإبلاغ عن المخاطر وتجميع المعلومات.",
"app_version":"الإصدار 1.0",
"clear":"مسح الإشعارات",
"yes":"نعم",
"cancel":"إلغاء",
"notification_new":"بلاغ جديد",
"status":"الحالة",
"date":"التاريخ"
}
}


EXTRA_T={'fr': {'vehicles': 'Vehicules', 'events': 'Programme', 'emergency_contacts': "Contacts d'urgence", 'team': 'Equipe', 'profile': 'Mon profil', 'vehicle_name': 'Nom / matricule', 'driver': 'Conducteur', 'add_vehicle': 'Ajouter vehicule', 'add_event': 'Ajouter activite', 'event_title': 'Titre', 'event_date': 'Date et heure', 'event_place': 'Lieu', 'add_contact': 'Ajouter contact', 'contact_name': 'Nom du contact', 'contact_phone': 'Numero du contact', 'notes': 'Notes', 'add_note': 'Ajouter une note', 'sos': 'SOS URGENCE', 'attach': 'Ajouter une photo', 'photo': 'Photo', 'export': 'Exporter les donnees', 'call': 'Appeler', 'ready': 'Pret', 'maintenance': 'Maintenance', 'problem': 'Probleme'}, 'en': {'vehicles': 'Vehicles', 'events': 'Schedule', 'emergency_contacts': 'Emergency contacts', 'team': 'Team', 'profile': 'My profile', 'vehicle_name': 'Name / plate', 'driver': 'Driver', 'add_vehicle': 'Add vehicle', 'add_event': 'Add activity', 'event_title': 'Title', 'event_date': 'Date and time', 'event_place': 'Place', 'add_contact': 'Add contact', 'contact_name': 'Contact name', 'contact_phone': 'Phone', 'notes': 'Notes', 'add_note': 'Add note', 'sos': 'EMERGENCY SOS', 'attach': 'Add a photo', 'photo': 'Photo', 'export': 'Export data', 'call': 'Call', 'ready': 'Ready', 'maintenance': 'Maintenance', 'problem': 'Problem'}, 'ar': {'vehicles': 'السيارات', 'events': 'البرنامج', 'emergency_contacts': 'جهات اتصال للطوارئ', 'team': 'الفريق', 'profile': 'ملفي', 'vehicle_name': 'اسم / رقم السيارة', 'driver': 'السائق', 'add_vehicle': 'إضافة سيارة', 'add_event': 'إضافة نشاط', 'event_title': 'العنوان', 'event_date': 'التاريخ والوقت', 'event_place': 'المكان', 'add_contact': 'إضافة جهة اتصال', 'contact_name': 'اسم جهة الاتصال', 'contact_phone': 'الهاتف', 'notes': 'ملاحظات', 'add_note': 'إضافة ملاحظة', 'sos': 'نجدة عاجلة', 'attach': 'إضافة صورة', 'photo': 'الصورة', 'export': 'تصدير البيانات', 'call': 'اتصال', 'ready': 'جاهزة', 'maintenance': 'صيانة', 'problem': 'عطب'}}

for _lang, _vals in {
    'fr': {
        'operations':'Centre de pilotage', 'tasks':'Missions', 'stock':'Stock sanitaire', 'broadcast':'Message equipe',
        'checklist':'Checklist depart', 'attendance':'Presence equipe', 'supplies':'Materiel', 'priority_task':'Priorite mission',
        'task_title':'Mission / tache', 'assigned':'Responsable', 'done':'Terminee', 'pending':'En attente', 'send_message':'Envoyer le message',
        'message':'Message', 'item':'Article', 'quantity':'Quantite', 'minimum':'Seuil minimum', 'low_stock':'Stock faible',
        'checked':'Verifie', 'unchecked':'A verifier', 'today':'Aujourd’hui', 'control':'Controle', 'add_task':'Ajouter mission',
        'add_stock':'Ajouter article', 'complete':'Terminer', 'reopen':'Rouvrir', 'team_present':'Presents', 'team_absent':'Absents',
        'communication':'Communication', 'medical_team':'Equipe medicale', 'transport':'Transport', 'logistics':'Logistique',
        'security_team':'Securite', 'route':'Itineraire / etapes', 'vehicle_status':'Etat'
    },
    'en': {
        'operations':'Operations center', 'tasks':'Missions', 'stock':'Medical stock', 'broadcast':'Team message',
        'checklist':'Departure checklist', 'attendance':'Team attendance', 'supplies':'Supplies', 'priority_task':'Mission priority',
        'task_title':'Mission / task', 'assigned':'Responsible', 'done':'Completed', 'pending':'Pending', 'send_message':'Send message',
        'message':'Message', 'item':'Item', 'quantity':'Quantity', 'minimum':'Minimum threshold', 'low_stock':'Low stock',
        'checked':'Checked', 'unchecked':'To check', 'today':'Today', 'control':'Control', 'add_task':'Add mission',
        'add_stock':'Add item', 'complete':'Complete', 'reopen':'Reopen', 'team_present':'Present', 'team_absent':'Absent',
        'communication':'Communication', 'medical_team':'Medical team', 'transport':'Transport', 'logistics':'Logistics',
        'security_team':'Security', 'route':'Route / stages', 'vehicle_status':'Status'
    },
    'ar': {
        'operations':'مركز القيادة والتنظيم', 'tasks':'المهام', 'stock':'المخزون الصحي', 'broadcast':'رسالة للفريق',
        'checklist':'قائمة التحقق قبل الانطلاق', 'attendance':'حضور الفريق', 'supplies':'المعدات', 'priority_task':'أولوية المهمة',
        'task_title':'المهمة / العمل', 'assigned':'المسؤول', 'done':'مكتملة', 'pending':'في الانتظار', 'send_message':'إرسال الرسالة',
        'message':'الرسالة', 'item':'المادة', 'quantity':'الكمية', 'minimum':'الحد الأدنى', 'low_stock':'مخزون منخفض',
        'checked':'تم التحقق', 'unchecked':'يجب التحقق', 'today':'اليوم', 'control':'مراقبة', 'add_task':'إضافة مهمة',
        'add_stock':'إضافة مادة', 'complete':'إنهاء', 'reopen':'إعادة فتح', 'team_present':'الحاضرون', 'team_absent':'الغائبون',
        'communication':'الاتصال', 'medical_team':'الفريق الصحي', 'transport':'النقل', 'logistics':'اللوجستيك',
        'security_team':'الأمن', 'route':'المسار / المراحل', 'vehicle_status':'الحالة'
    }
}.items():
    EXTRA_T[_lang].update(_vals)

# ============================================================
# DATA
# ============================================================

DEFAULT_DATA = {
    "language":"fr",
    "server":"",
    "participants":[],
    "tasks":[], "stock":[], "checklist":{}, "broadcasts":[],
    "reports":[],
    "notifications":[],
    "health":"good",
    "ambulance":"available",
    "vehicles":[], "events":[], "emergency_contacts":[], "team_notes":[],
    "profile":{"name":"","phone":"","role":"member"}
}


def data_file():
    return os.path.join(App.get_running_app().user_data_dir,
                        "smart_caravan_data.json")


def load_data():
    try:
        with open(data_file(), "r", encoding="utf-8") as f:
            data = json.load(f)
        for k, v in DEFAULT_DATA.items():
            if k not in data:
                data[k] = v
        return data
    except Exception:
        return copy.deepcopy(DEFAULT_DATA)


def save_data(data):
    os.makedirs(os.path.dirname(data_file()), exist_ok=True)
    with open(data_file(), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ============================================================
# VISUAL HELPERS
# ============================================================

class Card(BoxLayout):
    def __init__(self, bg=WHITE, radius=18, **kwargs):
        super().__init__(**kwargs)
        self.padding = dp(12)
        with self.canvas.before:
            Color(*bg)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(radius)]
            )
            Color(0.86, 0.89, 0.94, 1)
            self.border = Line(
                rounded_rectangle=(
                    self.x, self.y,
                    self.width, self.height,
                    dp(radius)
                ),
                width=0.7
            )
        self.bind(pos=self._update, size=self._update)

    def _update(self, *_):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.rounded_rectangle = (
            self.x, self.y,
            self.width, self.height,
            dp(18)
        )


class SCLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = kwargs.get("color", TEXT)
        self.halign = kwargs.get("halign", "left")
        self.valign = kwargs.get("valign", "middle")
        self.bind(size=self._align)

    def _align(self, *_):
        self.text_size = (self.width, None)


class SCButton(Button):
    def __init__(self, bg=BLUE, radius=14, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.color = WHITE
        self.font_size = dp(14)
        self.bold = True
        self.size_hint_y = None
        self.height = dp(54)

        with self.canvas.before:
            Color(*bg)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(radius)]
            )
        self.bind(pos=self._update, size=self._update)

    def _update(self, *_):
        self.rect.pos = self.pos
        self.rect.size = self.size


class SCInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_active = ""
        self.background_color = WHITE
        self.foreground_color = TEXT
        self.cursor_color = BLUE
        self.padding = [dp(13), dp(13)]
        self.font_size = dp(14)
        self.size_hint_y = None
        self.height = dp(52)


def local_notify(title, message):
    try:
        from plyer import notification
        notification.notify(title=title, message=message, app_name="SMART CARAVAN", timeout=5)
    except Exception:
        pass

def server_base(url):
    url=(url or "").strip().rstrip("/")
    if url.endswith("/api"): url=url[:-4]
    return url

def post_server_notification(base, payload):
    try:
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req=urllib.request.Request(base+"/notify", data=data, headers={"Content-Type":"application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=4) as r: return r.status == 200
    except Exception:
        return False

def fetch_server_notifications(base, since):
    try:
        with urllib.request.urlopen(base+"/notifications?since="+urllib.parse.quote(str(since)), timeout=4) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception:
        return []

def popup(title, message):
    box = BoxLayout(
        orientation="vertical",
        padding=dp(14),
        spacing=dp(10)
    )
    box.add_widget(Label(
        text=message,
        color=TEXT,
        halign="center",
        valign="middle"
    ))
    ok = SCButton(text="OK", bg=BLUE)
    box.add_widget(ok)

    p = Popup(
        title=title,
        content=box,
        size_hint=(.88, .34)
    )
    ok.bind(on_release=p.dismiss)
    p.open()


# ============================================================
# HEADER
# ============================================================

class Header(BoxLayout):
    def __init__(self, title, **kwargs):
        super().__init__(
            orientation="horizontal",
            spacing=dp(7),
            size_hint_y=None,
            height=dp(58),
            **kwargs
        )
        back = SCButton(text="<", bg=NAVY, width=dp(50))
        back.size_hint_x = None
        back.bind(on_release=lambda *_: App.get_running_app().go_to("dashboard"))
        self.add_widget(back)
        self.add_widget(Label(
            text=title,
            color=NAVY,
            bold=True,
            font_size=dp(20)
        ))


# ============================================================
# LOGIN
# ============================================================

class LoginScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()
        f = current_font(app.lang())

        root = BoxLayout(
            orientation="vertical",
            padding=[dp(25), dp(20), dp(25), dp(12)],
            spacing=dp(10)
        )

        # Decorative logo made entirely with Kivy shapes/text.
        logo = Card(
            bg=BLUE,
            orientation="vertical",
            size_hint_y=None,
            height=dp(135)
        )
        logo.add_widget(Label(
            text="SC",
            color=WHITE,
            bold=True,
            font_size=dp(46)
        ))
        logo.add_widget(Label(
            text=app.t("title"),
            color=WHITE,
            bold=True,
            font_size=dp(20)
        ))
        root.add_widget(logo)

        root.add_widget(Label(
            text=app.t("subtitle"),
            color=MUTED,
            font_size=dp(13),
            size_hint_y=None,
            height=dp(35)
        ))

        self.user = SCInput(
            hint_text=app.t("username"),
            multiline=False
        )
        self.password = SCInput(
            hint_text=app.t("password"),
            password=True,
            multiline=False
        )
        root.add_widget(self.user)
        root.add_widget(self.password)

        root.add_widget(SCButton(
            text=app.t("connect"),
            bg=BLUE,
            height=dp(58),
            on_release=self.login
        ))

        root.add_widget(Label(
            text=app.t("demo"),
            color=MUTED,
            font_size=dp(10),
            halign="center",
            size_hint_y=None,
            height=dp(48)
        ))

        lang = Spinner(
            text={"fr":"Français", "en":"English", "ar":"العربية"}[
                app.lang()
            ],
            values=("Français", "English", "العربية"),
            background_normal="",
            background_color=LIGHTBLUE,
            color=NAVY,
            size_hint_y=None,
            height=dp(50)
        )
        lang.bind(text=self.change_language)
        root.add_widget(lang)

        self.add_widget(root)

    def change_language(self, _, value):
        app = App.get_running_app()
        app.data["language"] = {
            "Français":"fr",
            "English":"en",
            "العربية":"ar"
        }.get(value, "fr")
        save_data(app.data)
        self.on_pre_enter()

    def login(self, *_):
        app = App.get_running_app()
        name = self.user.text.strip().lower()
        if name in ("admin", "leader", "member") and self.password.text == "1234":
            app.role = name
            app.sm.current = "dashboard"
        else:
            popup(app.t("login"), app.t("wrong"))


# ============================================================
# DASHBOARD
# ============================================================

class DashboardScreen(Screen):
    """Stable dashboard based on the known-working 4.5 screen architecture."""
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()
        reports = app.data.get("reports", []) or []
        participants = app.data.get("participants", []) or []
        vehicles = app.data.get("vehicles", []) or []
        tasks = app.data.get("tasks", []) or []
        checklist_items = app.data.get("checklist_items", {}) or {}
        opened = sum(1 for r in reports if r.get("status") != "resolved")
        critical = sum(1 for r in reports if r.get("priority") == "critical" and r.get("status") != "resolved")
        pending_tasks = sum(1 for t in tasks if not t.get("done") and t.get("status") != "done")
        done_check = sum(1 for v in checklist_items.values() if isinstance(v, dict) and v.get("done"))
        total_check = len(getattr(ChecklistScreen, "ITEMS", []))

        scroll = ScrollView(do_scroll_x=False, bar_width=dp(4))
        root = BoxLayout(orientation="vertical", spacing=dp(9), padding=[dp(10), dp(10), dp(10), dp(18)], size_hint_y=None)
        root.bind(minimum_height=root.setter("height"))

        # Header
        hero = Card(orientation="horizontal", bg=NAVY, size_hint_y=None, height=dp(100), padding=dp(10), spacing=dp(10))
        logo = ensure_logo()
        if logo:
            hero.add_widget(Image(source=logo, size_hint_x=None, width=dp(72), allow_stretch=True, keep_ratio=True))
        info = BoxLayout(orientation="vertical", spacing=dp(2))
        info.add_widget(Label(text="SMART CARAVAN", color=WHITE, bold=True, font_size=dp(20), halign="left"))
        info.add_widget(Label(text="CENTRE DE COMMANDE", color=CYAN, bold=True, font_size=dp(10), halign="left"))
        info.add_widget(Label(text="Leadership • Organisation • Santé • Sécurité", color=WHITE, font_size=dp(9), halign="left"))
        hero.add_widget(info)
        root.add_widget(hero)

        # Status strip
        status = Card(orientation="horizontal", bg=LIGHTGREEN, size_hint_y=None, height=dp(48), padding=dp(7), spacing=dp(6))
        status.add_widget(Label(text="LIVE", color=GREEN, bold=True, size_hint_x=None, width=dp(48), font_size=dp(11)))
        status.add_widget(Label(text="Participants: %d" % len(participants), color=TEXT, font_size=dp(9)))
        status.add_widget(Label(text="Véhicules: %d" % len(vehicles), color=TEXT, font_size=dp(9)))
        status.add_widget(Label(text="Alertes: %d" % opened, color=RED if opened else GREEN, bold=True, font_size=dp(9)))
        root.add_widget(status)

        # Emergency
        root.add_widget(Label(text="URGENCE", color=RED, bold=True, font_size=dp(13), size_hint_y=None, height=dp(23)))
        urgent = GridLayout(cols=2, spacing=dp(7), size_hint_y=None, height=dp(55))
        for label, target in (("SIGNALER UN DANGER", "danger"), ("SOS", "sos")):
            b = SCButton(text=label, bg=RED, height=dp(52))
            b.bind(on_release=lambda _btn, t=target: app.go_to(t))
            urgent.add_widget(b)
        root.add_widget(urgent)

        # Command KPIs
        root.add_widget(Label(text="ÉTAT DE LA CARAVANE", color=NAVY, bold=True, font_size=dp(13), size_hint_y=None, height=dp(23)))
        kpis = GridLayout(cols=2, spacing=dp(7), size_hint_y=None, height=dp(122))
        for title, value, color, target in (
            ("Alertes ouvertes", opened, ORANGE, "reports"),
            ("Alertes critiques", critical, RED, "reports"),
            ("Missions à faire", pending_tasks, BLUE, "tasks"),
            ("Check-list", "%d/%d" % (done_check, total_check), GREEN, "checklist"),
        ):
            card = Card(orientation="vertical", bg=WHITE, padding=dp(5))
            card.add_widget(Label(text=str(value), color=color, bold=True, font_size=dp(19)))
            card.add_widget(Label(text=title, color=MUTED, font_size=dp(9)))
            btn = Button(text="Ouvrir", background_normal="", background_color=(0,0,0,0), color=color, size_hint_y=None, height=dp(20), font_size=dp(9))
            btn.bind(on_release=lambda _btn, t=target: app.go_to(t))
            card.add_widget(btn)
            kpis.add_widget(card)
        root.add_widget(kpis)

        # Operations
        root.add_widget(Label(text="PILOTAGE & ORGANISATION", color=NAVY, bold=True, font_size=dp(13), size_hint_y=None, height=dp(23)))
        ops = GridLayout(cols=2, spacing=dp(7), size_hint_y=None, height=dp(165))
        for label, color, target in (
            ("Check-list départ", GREEN, "checklist"),
            ("Missions", BLUE, "tasks"),
            ("Centre des opérations", NAVY, "operations"),
            ("Participants", TEAL, "participants"),
            ("Véhicules", CYAN, "vehicles"),
            ("Caravane sanitaire", GREEN, "health"),
        ):
            b = SCButton(text=label, bg=color, height=dp(49))
            b.bind(on_release=lambda _btn, t=target: app.go_to(t))
            ops.add_widget(b)
        root.add_widget(ops)

        # Communication and follow-up
        root.add_widget(Label(text="SUIVI & COMMUNICATION", color=NAVY, bold=True, font_size=dp(13), size_hint_y=None, height=dp(23)))
        follow = GridLayout(cols=2, spacing=dp(7), size_hint_y=None, height=dp(165))
        for label, color, target in (
            ("Messages équipe", ORANGE, "broadcast"),
            ("Notifications", PURPLE, "notifications"),
            ("Rapports", BLUE, "reports"),
            ("Programme", ORANGE, "events"),
            ("Stock matériel", PURPLE, "stock"),
            ("Contacts urgence", RED, "contacts"),
        ):
            b = SCButton(text=label, bg=color, height=dp(49))
            b.bind(on_release=lambda _btn, t=target: app.go_to(t))
            follow.add_widget(b)
        root.add_widget(follow)

        bottom = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(7))
        for label, target in (("Profil", "profile"), ("Paramètres", "settings")):
            b = SCButton(text=label, bg=TEXT, height=dp(46))
            b.bind(on_release=lambda _btn, t=target: app.go_to(t))
            bottom.add_widget(b)
        root.add_widget(bottom)

        scroll.add_widget(root)
        self.add_widget(scroll)

    def go_to(self, target):
        app = App.get_running_app()
        app.go_to(target)

class DangerScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()

        root = BoxLayout(
            orientation="vertical", padding=dp(10), spacing=dp(8)
        )
        root.add_widget(Header(app.t("danger")))

        alert = Card(
            orientation="vertical",
            bg=LIGHTRED,
            size_hint_y=None,
            height=dp(75)
        )
        alert.add_widget(Label(
            text="ALERTE",
            color=RED, bold=True, font_size=dp(20)
        ))
        alert.add_widget(Label(
            text=app.t("danger") + " - " + app.t("reports"),
            color=RED, font_size=dp(11)
        ))
        root.add_widget(alert)

        scroll = ScrollView(do_scroll_x=False)
        form = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=[dp(3), dp(3), dp(3), dp(15)],
            size_hint_y=None
        )
        form.bind(minimum_height=form.setter("height"))

        def field_label(txt):
            return Label(
                text=txt, color=NAVY, bold=True, font_size=dp(12),
                size_hint_y=None, height=dp(25), halign="left"
            )

        form.add_widget(field_label(app.t("name")))
        self.reporter_name = SCInput(
            hint_text=app.t("name"), multiline=False
        )
        form.add_widget(self.reporter_name)

        form.add_widget(field_label(app.t("danger_type")))
        self.type = Spinner(
            text=app.t("accident"),
            values=(
                app.t("accident"), app.t("fire"), app.t("security"),
                app.t("medical"), app.t("vehicle"), app.t("road"),
                app.t("crowd"), app.t("other")
            ),
            background_normal="", background_color=LIGHTBLUE,
            color=TEXT, size_hint_y=None, height=dp(52)
        )
        form.add_widget(self.type)

        form.add_widget(field_label(app.t("priority")))
        self.priority = Spinner(
            text=app.t("high"),
            values=(
                app.t("low"), app.t("medium"),
                app.t("high"), app.t("critical")
            ),
            background_normal="", background_color=LIGHTORANGE,
            color=TEXT, size_hint_y=None, height=dp(52)
        )
        form.add_widget(self.priority)

        priority_row = GridLayout(
            cols=4, spacing=dp(5),
            size_hint_y=None, height=dp(45)
        )
        for value, color in (
            (app.t("low"), GREEN),
            (app.t("medium"), BLUE),
            (app.t("high"), ORANGE),
            (app.t("critical"), RED)
        ):
            b = SCButton(text=value, bg=color, height=dp(42))
            b.bind(
                on_release=lambda _, x=value:
                setattr(self.priority, "text", x)
            )
            priority_row.add_widget(b)
        form.add_widget(priority_row)

        form.add_widget(field_label(app.t("location")))
        self.location = SCInput(
            hint_text=app.t("location"), multiline=False
        )
        form.add_widget(self.location)

        form.add_widget(field_label(app.t("description")))
        self.description = SCInput(
            hint_text=app.t("description"),
            multiline=True, size_hint_y=None, height=dp(130)
        )
        form.add_widget(self.description)

        form.add_widget(field_label("Type rapide"))
        quick = GridLayout(
            cols=2, spacing=dp(6),
            size_hint_y=None, height=dp(98)
        )
        for value, color in (
            (app.t("accident"), RED),
            (app.t("medical"), GREEN),
            (app.t("fire"), ORANGE),
            (app.t("security"), PURPLE)
        ):
            b = SCButton(text=value, bg=color, height=dp(45))
            b.bind(
                on_release=lambda _, x=value:
                setattr(self.type, "text", x)
            )
            quick.add_widget(b)
        form.add_widget(quick)

        send = SCButton(
            text=app.t("send").upper(),
            bg=RED, height=dp(64)
        )
        send.bind(on_release=self.send)
        form.add_widget(send)

        scroll.add_widget(form)
        root.add_widget(scroll)
        self.add_widget(root)

    def send(self, *_):
        app = App.get_running_app()

        name = self.reporter_name.text.strip()
        description = self.description.text.strip()

        if not name or not description:
            popup(app.t("danger"), app.t("required"))
            return

        type_map = {
            app.t("accident"): "accident",
            app.t("fire"): "fire",
            app.t("security"): "security",
            app.t("medical"): "medical",
            app.t("vehicle"): "vehicle",
            app.t("road"): "road",
            app.t("crowd"): "crowd",
            app.t("other"): "other"
        }
        priority_map = {
            app.t("low"): "low",
            app.t("medium"): "medium",
            app.t("high"): "high",
            app.t("critical"): "critical"
        }

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = {
            "id": int(datetime.now().timestamp() * 1000),
            "name": name,
            "type": type_map.get(self.type.text, "other"),
            "priority": priority_map.get(self.priority.text, "high"),
            "location": self.location.text.strip(),
            "description": description,
            "status": "open",
            "date": now
        }

        app.data.setdefault("reports", []).append(report)
        app.data.setdefault("notifications", []).insert(0, {
            "title": app.t("notification_new"),
            "message": report["type"].upper() + " | " +
                       report["priority"].upper() + "\n" + description,
            "date": now
        })
        save_data(app.data)
        local_notify("SMART CARAVAN", report["type"].upper() + " | " + report["priority"].upper())
        base = server_base(app.data.get("server", ""))
        if base:
            payload = {"title": app.t("notification_new"), "message": report["type"].upper() + " | " + report["priority"].upper() + "\n" + description, "date": now}
            threading.Thread(target=post_server_notification, args=(base, payload), daemon=True).start()

        popup(
            app.t("danger"),
            app.t("saved") + "\n" +
            "ID: " + str(report["id"])
        )

        self.reporter_name.text = ""
        self.location.text = ""
        self.description.text = ""
        self.type.text = app.t("accident")
        self.priority.text = app.t("high")
        app.sm.current = "dashboard"


# ============================================================
# PARTICIPANTS
# ============================================================

class ParticipantsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )
        root.add_widget(Header(app.t("participants")))
        root.add_widget(SCButton(
            text="+  " + app.t("add"),
            bg=GREEN,
            on_release=self.add_person
        ))

        scroll = ScrollView()
        self.list = GridLayout(
            cols=1,
            spacing=dp(8),
            size_hint_y=None
        )
        self.list.bind(minimum_height=self.list.setter("height"))
        scroll.add_widget(self.list)
        root.add_widget(scroll)

        self.add_widget(root)
        self.refresh()

    def refresh(self):
        app = App.get_running_app()
        self.list.clear_widgets()

        if not app.data["participants"]:
            self.list.add_widget(Label(
                text=app.t("no_data"),
                color=MUTED,
                size_hint_y=None,
                height=dp(60)
            ))
            return

        for index, person in enumerate(app.data["participants"]):
            row = Card(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(72)
            )
            row.add_widget(Label(
                text=person["name"] + "\n" + person["phone"] + "\n" + (app.t("team_present") if person.get("present", True) else app.t("team_absent")),
                color=TEXT,
                font_size=dp(13)
            ))
            toggle = SCButton(text=app.t("team_present") if person.get("present", True) else app.t("team_absent"),
                              bg=GREEN if person.get("present", True) else ORANGE, width=dp(92), height=dp(42))
            toggle.size_hint_x = None
            toggle.bind(on_release=lambda _, i=index: self.toggle_presence(i))
            row.add_widget(toggle)
            delete = SCButton(text=app.t("delete"), bg=RED, width=dp(78), height=dp(42))
            delete.size_hint_x = None
            delete.bind(on_release=lambda _, i=index: self.remove(i))
            row.add_widget(delete)
            self.list.add_widget(row)

    def toggle_presence(self, index):
        app = App.get_running_app()
        if 0 <= index < len(app.data["participants"]):
            app.data["participants"][index]["present"] = not app.data["participants"][index].get("present", True)
            save_data(app.data)
            self.refresh()

    def add_person(self, *_):
        app = App.get_running_app()

        box = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(8)
        )
        name = SCInput(
            hint_text=app.t("name"),
            multiline=False
        )
        phone = SCInput(
            hint_text=app.t("phone"),
            multiline=False
        )
        box.add_widget(name)
        box.add_widget(phone)

        buttons = BoxLayout(
            size_hint_y=None,
            height=dp(52),
            spacing=dp(7)
        )
        cancel = SCButton(text=app.t("cancel"), bg=NAVY)
        save = SCButton(text=app.t("save"), bg=GREEN)
        buttons.add_widget(cancel)
        buttons.add_widget(save)
        box.add_widget(buttons)

        p = Popup(
            title=app.t("add"),
            content=box,
            size_hint=(.90, .50)
        )
        cancel.bind(on_release=p.dismiss)

        def save_person(*_):
            if not name.text.strip():
                return
            app.data["participants"].append({
                "name":name.text.strip(),
                "phone":phone.text.strip(),
                "present":True
            })
            save_data(app.data)
            p.dismiss()
            self.refresh()

        save.bind(on_release=save_person)
        p.open()

    def remove(self, index):
        app = App.get_running_app()
        if 0 <= index < len(app.data["participants"]):
            app.data["participants"].pop(index)
            save_data(app.data)
            self.refresh()


# ============================================================
# HEALTH
# ============================================================

class HealthScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10)
        )
        root.add_widget(Header(app.t("health")))

        card = Card(
            orientation="vertical",
            size_hint_y=None,
            height=dp(175)
        )
        card.add_widget(Label(
            text="MEDICAL",
            color=GREEN,
            bold=True,
            font_size=dp(24)
        ))
        card.add_widget(Label(
            text=app.t("health_status"),
            color=NAVY,
            font_size=dp(17)
        ))

        self.health = Spinner(
            text={
                "good":app.t("good"),
                "watch":app.t("watch"),
                "emergency":app.t("emergency")
            }.get(app.data.get("health"), app.t("good")),
            values=(
                app.t("good"),
                app.t("watch"),
                app.t("emergency")
            ),
            background_normal="",
            background_color=LIGHTGREEN,
            color=TEXT,
            size_hint_y=None,
            height=dp(52)
        )
        card.add_widget(self.health)
        root.add_widget(card)

        amb = Card(
            orientation="vertical",
            size_hint_y=None,
            height=dp(140)
        )
        amb.add_widget(Label(
            text=app.t("ambulance"),
            color=BLUE,
            bold=True,
            font_size=dp(19)
        ))
        self.ambulance = Spinner(
            text={
                "available":app.t("available"),
                "busy":app.t("busy")
            }.get(app.data.get("ambulance"), app.t("available")),
            values=(app.t("available"), app.t("busy")),
            background_normal="",
            background_color=LIGHTBLUE,
            color=TEXT,
            size_hint_y=None,
            height=dp(52)
        )
        amb.add_widget(self.ambulance)
        root.add_widget(amb)

        readiness = Card(orientation="vertical", bg=LIGHTBLUE, size_hint_y=None, height=dp(90))
        readiness.add_widget(Label(text=app.t("medical_team"), color=BLUE, bold=True, font_size=dp(14)))
        readiness.add_widget(Label(text=app.t("health_status") + " • " + app.t("ambulance"), color=TEXT, font_size=dp(10)))
        root.add_widget(readiness)

        root.add_widget(SCButton(
            text=app.t("save"),
            bg=GREEN,
            on_release=self.save
        ))

        self.add_widget(root)

    def save(self, *_):
        app = App.get_running_app()

        health = {
            app.t("good"):"good",
            app.t("watch"):"watch",
            app.t("emergency"):"emergency"
        }
        ambulance = {
            app.t("available"):"available",
            app.t("busy"):"busy"
        }

        app.data["health"] = health.get(self.health.text, "good")
        app.data["ambulance"] = ambulance.get(
            self.ambulance.text, "available")
        save_data(app.data)

        popup(app.t("health"), app.t("saved"))


# ============================================================
# NOTIFICATIONS
# ============================================================

class NotificationsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )
        root.add_widget(Header(app.t("notifications")))

        root.add_widget(SCButton(
            text=app.t("clear"),
            bg=PURPLE,
            height=dp(48),
            on_release=self.clear
        ))

        scroll = ScrollView()
        self.list = GridLayout(
            cols=1,
            spacing=dp(8),
            size_hint_y=None
        )
        self.list.bind(minimum_height=self.list.setter("height"))
        scroll.add_widget(self.list)
        root.add_widget(scroll)

        self.add_widget(root)
        self.refresh()

    def refresh(self):
        app = App.get_running_app()
        self.list.clear_widgets()

        if not app.data["notifications"]:
            self.list.add_widget(Label(
                text=app.t("no_data"),
                color=MUTED,
                size_hint_y=None,
                height=dp(60)
            ))
            return

        for n in app.data["notifications"]:
            c = Card(
                orientation="vertical",
                size_hint_y=None,
                height=dp(100),
                bg=LIGHTPURPLE
            )
            c.add_widget(Label(
                text=n["title"],
                color=PURPLE,
                bold=True,
                font_size=dp(15)
            ))
            c.add_widget(Label(
                text=n["message"] + "\n" + n["date"],
                color=TEXT,
                font_size=dp(12)
            ))
            self.list.add_widget(c)

    def clear(self, *_):
        app = App.get_running_app()
        app.data["notifications"] = []
        save_data(app.data)
        self.refresh()


# ============================================================
# REPORTS
# ============================================================

class ReportsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )
        root.add_widget(Header(app.t("reports")))

        scroll = ScrollView()
        self.list = GridLayout(
            cols=1,
            spacing=dp(8),
            size_hint_y=None
        )
        self.list.bind(minimum_height=self.list.setter("height"))
        scroll.add_widget(self.list)
        root.add_widget(scroll)

        self.add_widget(root)
        self.refresh()

    def refresh(self):
        app = App.get_running_app()
        self.list.clear_widgets()

        reports = list(reversed(app.data["reports"]))

        if not reports:
            self.list.add_widget(Label(
                text=app.t("no_data"),
                color=MUTED,
                size_hint_y=None,
                height=dp(60)
            ))
            return

        for report in reports:
            color = RED if report["priority"] == "critical" else ORANGE
            bg = LIGHTRED if report["priority"] == "critical" else LIGHTORANGE

            c = Card(
                orientation="vertical",
                size_hint_y=None,
                height=dp(168),
                bg=bg
            )

            c.add_widget(Label(
                text=report["type"].upper() +
                     "   •   " +
                     report["priority"].upper(),
                color=color,
                bold=True,
                font_size=dp(14)
            ))
            c.add_widget(Label(
                text=report["name"] +
                     "\n" + report["description"] +
                     "\n" + report["location"] +
                     "\n" + report["date"],
                color=TEXT,
                font_size=dp(11)
            ))

            if report["status"] != "resolved":
                b = SCButton(
                    text=app.t("resolve"),
                    bg=GREEN,
                    height=dp(38)
                )
                b.bind(
                    on_release=lambda _, r=report:
                    self.resolve(r)
                )
                c.add_widget(b)

            self.list.add_widget(c)

    def resolve(self, report):
        app = App.get_running_app()
        for r in app.data["reports"]:
            if r["id"] == report["id"]:
                r["status"] = "resolved"
                break
        save_data(app.data)
        self.refresh()


# ============================================================
# SETTINGS
# ============================================================

class SettingsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(9)
        )
        root.add_widget(Header(app.t("settings")))

        root.add_widget(Label(
            text=app.t("language"),
            color=NAVY,
            bold=True,
            font_size=dp(17),
            size_hint_y=None,
            height=dp(35)
        ))

        self.language = Spinner(
            text={"fr":"Français", "en":"English", "ar":"العربية"}[
                app.lang()
            ],
            values=("Français", "English", "العربية"),
            background_normal="",
            background_color=LIGHTBLUE,
            color=TEXT,
            size_hint_y=None,
            height=dp(52)
        )
        root.add_widget(self.language)

        root.add_widget(Label(
            text=app.t("server"),
            color=NAVY,
            bold=True,
            font_size=dp(17),
            size_hint_y=None,
            height=dp(35)
        ))

        self.server = SCInput(
            text=app.data.get("server", ""),
            hint_text=app.t("server_hint"),
            multiline=False
        )
        root.add_widget(self.server)

        root.add_widget(SCButton(
            text=app.t("save"),
            bg=GREEN,
            on_release=self.save
        ))

        root.add_widget(SCButton(
            text=app.t("sync"),
            bg=PURPLE,
            on_release=self.sync
        ))

        root.add_widget(Label(
            text=app.t("about") + "\n\n" + app.t("app_version"),
            color=MUTED,
            font_size=dp(11),
            halign="center"
        ))

        self.add_widget(root)

    def save(self, *_):
        app = App.get_running_app()

        app.data["language"] = {
            "Français":"fr",
            "English":"en",
            "العربية":"ar"
        }.get(self.language.text, "fr")

        app.data["server"] = self.server.text.strip()
        save_data(app.data)

        app.build_screens()
        app.sm.current = "settings"

    def sync(self, *_):
        app = App.get_running_app()
        if not app.data.get("server"):
            popup(app.t("sync"), app.t("not_connected"))
        else:
            popup(
                app.t("sync"),
                "API ready: " + app.data["server"]
            )


# ============================================================
# EXTENDED MODULES
# ============================================================

class VehiclesScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app()
        root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8))
        root.add_widget(Header(app.t("vehicles")))
        add=SCButton(text="+  "+app.t("add_vehicle"),bg=BLUE)
        add.bind(on_release=self.add); root.add_widget(add)
        sv=ScrollView(do_scroll_x=False)
        self.lst=GridLayout(cols=1,spacing=dp(8),size_hint_y=None)
        self.lst.bind(minimum_height=self.lst.setter("height")); sv.add_widget(self.lst)
        root.add_widget(sv); self.add_widget(root); self.refresh()
    def refresh(self):
        app=App.get_running_app(); self.lst.clear_widgets()
        if not app.data["vehicles"]:
            self.lst.add_widget(Label(text=app.t("no_data"),color=MUTED,size_hint_y=None,height=dp(60))); return
        for i,v in enumerate(app.data["vehicles"]):
            c=Card(orientation="vertical",bg=LIGHTGREEN if v.get("status")==app.t("ready") else LIGHTORANGE,size_hint_y=None,height=dp(125))
            c.add_widget(Label(text=v["name"],color=BLUE,bold=True,font_size=dp(16)))
            c.add_widget(Label(text=app.t("driver")+": "+v.get("driver","")+"\n"+app.t("vehicle_status")+": "+v.get("status",""),color=TEXT,font_size=dp(11)))
            b=SCButton(text=app.t("delete"),bg=RED,height=dp(35)); b.bind(on_release=lambda _,x=i:self.remove(x)); c.add_widget(b)
            self.lst.add_widget(c)
    def add(self,*_):
        app=App.get_running_app()
        box=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(7))
        name=SCInput(hint_text=app.t("vehicle_name"),multiline=False); driver=SCInput(hint_text=app.t("driver"),multiline=False)
        status=Spinner(text=app.t("ready"),values=(app.t("ready"),app.t("maintenance"),app.t("problem")),background_normal="",background_color=LIGHTBLUE,color=TEXT,size_hint_y=None,height=dp(52))
        box.add_widget(name); box.add_widget(driver); box.add_widget(status)
        btn=SCButton(text=app.t("save"),bg=GREEN); box.add_widget(btn)
        p=Popup(title=app.t("add_vehicle"),content=box,size_hint=(.9,.55))
        def go(_):
            if name.text.strip():
                app.data["vehicles"].append({"name":name.text.strip(),"driver":driver.text.strip(),"status":status.text})
                save_data(app.data); p.dismiss(); self.refresh()
        btn.bind(on_release=go); p.open()
    def remove(self,i):
        app=App.get_running_app()
        if 0<=i<len(app.data["vehicles"]): app.data["vehicles"].pop(i); save_data(app.data); self.refresh()


class EventsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app()
        root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8)); root.add_widget(Header(app.t("events")))
        b=SCButton(text="+  "+app.t("add_event"),bg=ORANGE); b.bind(on_release=self.add); root.add_widget(b)
        sv=ScrollView(do_scroll_x=False); self.lst=GridLayout(cols=1,spacing=dp(8),size_hint_y=None); self.lst.bind(minimum_height=self.lst.setter("height")); sv.add_widget(self.lst); root.add_widget(sv); self.add_widget(root); self.refresh()
    def refresh(self):
        app=App.get_running_app(); self.lst.clear_widgets()
        for i,e in enumerate(app.data["events"]):
            c=Card(orientation="vertical",bg=LIGHTORANGE,size_hint_y=None,height=dp(120))
            c.add_widget(Label(text=e["title"],color=ORANGE,bold=True,font_size=dp(16)))
            c.add_widget(Label(text=e["date"]+"  •  "+e["place"]+"\n"+e.get("notes",""),color=TEXT,font_size=dp(11)))
            b=SCButton(text=app.t("delete"),bg=RED,height=dp(34)); b.bind(on_release=lambda _,x=i:self.remove(x)); c.add_widget(b); self.lst.add_widget(c)
        if not app.data["events"]: self.lst.add_widget(Label(text=app.t("no_data"),color=MUTED,size_hint_y=None,height=dp(60)))
    def add(self,*_):
        app=App.get_running_app()
        box=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(7))
        a=SCInput(hint_text=app.t("event_title"),multiline=False); b=SCInput(hint_text=app.t("event_date"),multiline=False); c=SCInput(hint_text=app.t("event_place"),multiline=False); d=SCInput(hint_text=app.t("notes"),multiline=False)
        for x in (a,b,c,d): box.add_widget(x)
        save=SCButton(text=app.t("save"),bg=GREEN); box.add_widget(save); p=Popup(title=app.t("add_event"),content=box,size_hint=(.9,.7))
        def go(_):
            if a.text.strip():
                app.data["events"].append({"title":a.text.strip(),"date":b.text.strip(),"place":c.text.strip(),"notes":d.text.strip()}); save_data(app.data); p.dismiss(); self.refresh()
        save.bind(on_release=go); p.open()
    def remove(self,i):
        app=App.get_running_app()
        if 0<=i<len(app.data["events"]): app.data["events"].pop(i); save_data(app.data); self.refresh()


class ContactsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app()
        root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8)); root.add_widget(Header(app.t("emergency_contacts")))
        b=SCButton(text="+  "+app.t("add_contact"),bg=RED); b.bind(on_release=self.add); root.add_widget(b)
        sv=ScrollView(do_scroll_x=False); self.lst=GridLayout(cols=1,spacing=dp(8),size_hint_y=None); self.lst.bind(minimum_height=self.lst.setter("height")); sv.add_widget(self.lst); root.add_widget(sv); self.add_widget(root); self.refresh()
    def refresh(self):
        app=App.get_running_app(); self.lst.clear_widgets()
        for i,c in enumerate(app.data["emergency_contacts"]):
            row=Card(orientation="horizontal",bg=LIGHTRED,size_hint_y=None,height=dp(70))
            row.add_widget(Label(text=c["name"]+"\n"+c["phone"],color=TEXT,font_size=dp(11)))
            call=SCButton(text=app.t("call"),bg=GREEN,height=dp(40)); call.size_hint_x=None; call.width=dp(75); call.bind(on_release=lambda _,ph=c["phone"]:popup(app.t("call"),ph))
            delete=SCButton(text=app.t("delete"),bg=RED,height=dp(40)); delete.size_hint_x=None; delete.width=dp(75); delete.bind(on_release=lambda _,x=i:self.remove(x))
            row.add_widget(call); row.add_widget(delete); self.lst.add_widget(row)
        if not app.data["emergency_contacts"]: self.lst.add_widget(Label(text=app.t("no_data"),color=MUTED,size_hint_y=None,height=dp(60)))
    def add(self,*_):
        app=App.get_running_app()
        box=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(7)); a=SCInput(hint_text=app.t("contact_name"),multiline=False); b=SCInput(hint_text=app.t("contact_phone"),multiline=False); s=SCButton(text=app.t("save"),bg=GREEN)
        box.add_widget(a); box.add_widget(b); box.add_widget(s); p=Popup(title=app.t("add_contact"),content=box,size_hint=(.9,.48))
        def go(_):
            if a.text.strip() and b.text.strip(): app.data["emergency_contacts"].append({"name":a.text.strip(),"phone":b.text.strip()}); save_data(app.data); p.dismiss(); self.refresh()
        s.bind(on_release=go); p.open()
    def remove(self,i):
        app=App.get_running_app()
        if 0<=i<len(app.data["emergency_contacts"]): app.data["emergency_contacts"].pop(i); save_data(app.data); self.refresh()


class TeamScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app()
        root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8)); root.add_widget(Header(app.t("team")))
        self.note=SCInput(hint_text=app.t("notes"),multiline=True,size_hint_y=None,height=dp(115)); root.add_widget(self.note)
        s=SCButton(text=app.t("add_note"),bg=TEAL); s.bind(on_release=self.save_note); root.add_widget(s)
        sv=ScrollView(do_scroll_x=False); self.lst=GridLayout(cols=1,spacing=dp(7),size_hint_y=None); self.lst.bind(minimum_height=self.lst.setter("height")); sv.add_widget(self.lst); root.add_widget(sv); self.add_widget(root); self.refresh()
    def save_note(self,*_):
        app=App.get_running_app()
        if self.note.text.strip(): app.data["team_notes"].insert(0,{"text":self.note.text.strip(),"date":datetime.now().strftime("%Y-%m-%d %H:%M")}); save_data(app.data); self.note.text=""; self.refresh()
    def refresh(self):
        app=App.get_running_app(); self.lst.clear_widgets()
        for n in app.data["team_notes"]:
            c=Card(orientation="vertical",bg=LIGHTBLUE,size_hint_y=None,height=dp(75)); c.add_widget(Label(text=n["text"],color=TEXT,font_size=dp(11))); c.add_widget(Label(text=n["date"],color=MUTED,font_size=dp(9))); self.lst.add_widget(c)


class ProfileScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app(); p=app.data.get("profile",{})
        root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(9)); root.add_widget(Header(app.t("profile")))
        lp=ensure_logo()
        if lp:
            root.add_widget(Image(source=lp,size_hint_y=None,height=dp(90),allow_stretch=True,keep_ratio=True))
        self.profile_name=SCInput(text=p.get("name",""),hint_text=app.t("name"),multiline=False); self.phone=SCInput(text=p.get("phone",""),hint_text=app.t("phone"),multiline=False)
        self.role=Spinner(text=p.get("role",app.role),values=("admin","leader","member"),background_normal="",background_color=LIGHTBLUE,color=TEXT,size_hint_y=None,height=dp(52))
        root.add_widget(self.profile_name); root.add_widget(self.phone); root.add_widget(self.role); b=SCButton(text=app.t("save"),bg=GREEN); b.bind(on_release=self.save); root.add_widget(b); self.add_widget(root)
    def save(self,*_):
        app=App.get_running_app(); app.data["profile"]={"name":self.profile_name.text.strip(),"phone":self.phone.text.strip(),"role":self.role.text}; save_data(app.data); popup(app.t("profile"),app.t("saved"))


class SOSScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app()
        root=BoxLayout(orientation="vertical",padding=dp(18),spacing=dp(12)); root.add_widget(Header(app.t("sos")))
        root.add_widget(Label(text="SOS",color=RED,bold=True,font_size=dp(60)))
        b=SCButton(text=app.t("sos"),bg=RED,height=dp(80)); b.bind(on_release=self.send); root.add_widget(b)
        root.add_widget(Label(text=app.t("emergency_contacts"),color=MUTED,font_size=dp(12)))
        self.add_widget(root)
    def send(self,*_):
        app=App.get_running_app(); now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.data["notifications"].insert(0,{"title":"SOS","message":"Emergency SOS","date":now})
        app.data["reports"].append({"id":int(datetime.now().timestamp()*1000),"name":app.data.get("profile",{}).get("name","SOS"),"type":"medical","priority":"critical","location":"","description":"SOS emergency alert","status":"open","date":now})
        save_data(app.data)
        local_notify("SOS", "Emergency SOS")
        base = server_base(app.data.get("server", ""))
        if base:
            payload={"title":"SOS", "message":"Emergency SOS", "date":now}
            threading.Thread(target=post_server_notification, args=(base,payload), daemon=True).start()
        popup(app.t("sos"),app.t("saved"))



# ============================================================
# OPERATIONS / LEADERSHIP MODULES
# ============================================================

class OperationsScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app()
        root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8))
        root.add_widget(Header(app.t("operations")))
        reports=app.data.get("reports",[]); open_count=sum(1 for r in reports if r.get("status")!="resolved")
        tasks=app.data.get("tasks",[]); pending=sum(1 for t in tasks if not t.get("done"))
        low=sum(1 for s in app.data.get("stock",[]) if int(s.get("quantity",0))<=int(s.get("minimum",0)))
        stats=GridLayout(cols=3,spacing=dp(6),size_hint_y=None,height=dp(78))
        for title,value,color in ((app.t("open"),open_count,RED),(app.t("pending"),pending,ORANGE),(app.t("low_stock"),low,PURPLE)):
            c=Card(orientation="vertical",padding=dp(5)); c.add_widget(Label(text=str(value),color=color,bold=True,font_size=dp(20))); c.add_widget(Label(text=title,color=MUTED,font_size=dp(8))); stats.add_widget(c)
        root.add_widget(stats)
        scroll=ScrollView(do_scroll_x=False); grid=GridLayout(cols=2,spacing=dp(7),size_hint_y=None); grid.bind(minimum_height=grid.setter("height")); scroll.add_widget(grid); root.add_widget(scroll)
        modules=[(app.t("tasks"),BLUE,"tasks"),(app.t("checklist"),GREEN,"checklist"),(app.t("stock"),PURPLE,"stock"),(app.t("broadcast"),ORANGE,"broadcast"),(app.t("attendance"),TEAL,"participants"),(app.t("events"),CYAN,"events"),(app.t("vehicles"),BLUE,"vehicles"),(app.t("health"),GREEN,"health"),(app.t("emergency_contacts"),RED,"contacts")]
        for label,color,target in modules:
            b=SCButton(text=label,bg=color,height=dp(56)); b.bind(on_release=lambda _,t=target:self.go(t)); grid.add_widget(b)
        self.add_widget(root)
    def go(self,target): App.get_running_app().go_to(target)


class TasksScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app(); root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8)); root.add_widget(Header(app.t("tasks")))
        b=SCButton(text="+  "+app.t("add_task"),bg=BLUE); b.bind(on_release=self.add); root.add_widget(b)
        sv=ScrollView(do_scroll_x=False); self.lst=GridLayout(cols=1,spacing=dp(8),size_hint_y=None); self.lst.bind(minimum_height=self.lst.setter("height")); sv.add_widget(self.lst); root.add_widget(sv); self.add_widget(root); self.refresh()
    def refresh(self):
        app=App.get_running_app(); self.lst.clear_widgets()
        for i,t in enumerate(app.data.get("tasks",[])):
            done=t.get("done",False); bg=LIGHTGREEN if done else LIGHTBLUE
            c=Card(orientation="vertical",bg=bg,size_hint_y=None,height=dp(125)); c.add_widget(Label(text=t.get("title",""),color=GREEN if done else BLUE,bold=True,font_size=dp(15))); c.add_widget(Label(text=app.t("assigned")+": "+t.get("assigned","")+"\n"+app.t("priority")+": "+t.get("priority","medium"),color=TEXT,font_size=dp(10)))
            row=BoxLayout(size_hint_y=None,height=dp(38),spacing=dp(5)); b=SCButton(text=app.t("reopen") if done else app.t("complete"),bg=ORANGE if done else GREEN,height=dp(36)); b.bind(on_release=lambda _,x=i:self.toggle(x)); d=SCButton(text=app.t("delete"),bg=RED,height=dp(36)); d.bind(on_release=lambda _,x=i:self.remove(x)); row.add_widget(b); row.add_widget(d); c.add_widget(row); self.lst.add_widget(c)
        if not app.data.get("tasks"): self.lst.add_widget(Label(text=app.t("no_data"),color=MUTED,size_hint_y=None,height=dp(60)))
    def add(self,*_):
        app=App.get_running_app(); box=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(7)); title=SCInput(hint_text=app.t("task_title"),multiline=False); assigned=SCInput(hint_text=app.t("assigned"),multiline=False); priority=Spinner(text=app.t("medium"),values=(app.t("low"),app.t("medium"),app.t("high"),app.t("critical")),background_normal="",background_color=LIGHTBLUE,color=TEXT,size_hint_y=None,height=dp(52)); save=SCButton(text=app.t("save"),bg=GREEN); [box.add_widget(x) for x in (title,assigned,priority,save)]; p=Popup(title=app.t("add_task"),content=box,size_hint=(.9,.62))
        def go(_):
            if title.text.strip(): app.data.setdefault("tasks",[]).append({"title":title.text.strip(),"assigned":assigned.text.strip(),"priority":priority.text,"done":False,"date":datetime.now().strftime("%Y-%m-%d %H:%M")}); save_data(app.data); p.dismiss(); self.refresh()
        save.bind(on_release=go); p.open()
    def toggle(self,i):
        app=App.get_running_app();
        if 0<=i<len(app.data.get("tasks",[])): app.data["tasks"][i]["done"]=not app.data["tasks"][i].get("done",False); save_data(app.data); self.refresh()
    def remove(self,i):
        app=App.get_running_app();
        if 0<=i<len(app.data.get("tasks",[])): app.data["tasks"].pop(i); save_data(app.data); self.refresh()


class ChecklistScreen(Screen):
    # Full departure checklist designed for the leadership/organization team.
    ITEMS = [
        ("medical_team", "MEDICAL", "Equipe sanitaire: medecins, infirmiers, secouristes et responsable sante"),
        ("medical_kit", "MEDICAL", "Trousse de secours, medicaments autorises, gants, masques et consommables"),
        ("transport", "TRANSPORT", "Vehicules affectes, chauffeurs, carburant et documents des vehicules"),
        ("communication", "COMMUNICATION", "Telephones, batteries, chargeurs, groupes de communication et contacts"),
        ("logistics", "LOGISTIQUE", "Materiel, eau, nourriture, signalisation et besoins logistiques"),
        ("security_team", "SECURITE", "Equipe de securite, responsables de zones et procedure d'urgence"),
        ("route", "PARCOURS", "Etapes, points de rassemblement, horaires et acces aux sites"),
        ("attendance", "EQUIPE", "Presence des membres, responsables et affectations du jour"),
        ("documents", "ADMINISTRATION", "Autorisations, listes, contacts officiels et documents necessaires"),
        ("first_aid_point", "SANTE", "Point sanitaire identifie, acces ambulance et orientation des cas urgents"),
        ("water_food", "LOGISTIQUE", "Eau potable, repas, distribution et besoins particuliers"),
        ("media", "COMMUNICATION", "Photographie, communication, annonces et information du public"),
    ]

    def on_pre_enter(self):
        self.clear_widgets()
        app = App.get_running_app()
        root = BoxLayout(orientation="vertical", padding=dp(10), spacing=dp(7))
        root.add_widget(Header(app.t("checklist")))
        root.add_widget(Label(text="CHECK-LIST DEPART / LEADERSHIP & ORGANISATION", color=GREEN,
                              bold=True, font_size=dp(14), size_hint_y=None, height=dp(32)))
        root.add_widget(Label(text="Ouvrez chaque element pour affecter un responsable, ajouter une note et confirmer son etat.",
                              color=MUTED, font_size=dp(10), size_hint_y=None, height=dp(38)))

        sv = ScrollView(do_scroll_x=False)
        box = BoxLayout(orientation="vertical", spacing=dp(7), size_hint_y=None, padding=dp(2))
        box.bind(minimum_height=box.setter("height"))
        self.rows = {}
        self.items_data = app.data.setdefault("checklist_items", {})

        for key, category, desc in self.ITEMS:
            old = self.items_data.get(key, {})
            if isinstance(old, bool):
                old = {"done": old, "responsible": "", "notes": ""}
            row = Card(orientation="horizontal", bg=WHITE, size_hint_y=None, height=dp(78))
            cb = CheckBox(active=bool(old.get("done", False)), size_hint_x=None, width=dp(48))
            cb.bind(active=lambda widget, value, k=key: self.quick_check(k, value))
            row.add_widget(cb)
            info = BoxLayout(orientation="vertical", padding=(dp(5), dp(3)))
            info.add_widget(Label(text=category + "  •  " + app.t(key), color=TEXT, bold=True,
                                  font_size=dp(11), halign="left", valign="middle"))
            info.add_widget(Label(text=(old.get("responsible", "") or "Non affecte") +
                                       ("  |  " + (old.get("notes", "")[:45]) if old.get("notes") else ""),
                                  color=MUTED, font_size=dp(9), halign="left", valign="middle"))
            row.add_widget(info)
            detail = SCButton(text="DETAILS", bg=BLUE, height=dp(42), size_hint_x=None, width=dp(88))
            detail.bind(on_release=lambda _, k=key, c=category, d=desc: self.open_item(k, c, d))
            row.add_widget(detail)
            self.rows[key] = cb
            box.add_widget(row)

        sv.add_widget(box)
        root.add_widget(sv)
        bottom = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(6))
        save = SCButton(text=app.t("save"), bg=GREEN)
        reset = SCButton(text="RESET", bg=ORANGE)
        save.bind(on_release=self.save)
        reset.bind(on_release=self.reset_all)
        bottom.add_widget(save); bottom.add_widget(reset)
        root.add_widget(bottom)
        self.add_widget(root)

    def quick_check(self, key, value):
        app = App.get_running_app()
        data = app.data.setdefault("checklist_items", {})
        old = data.get(key, {})
        if isinstance(old, bool):
            old = {"done": old, "responsible": "", "notes": ""}
        old["done"] = bool(value)
        old["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        data[key] = old
        save_data(app.data)

    def open_item(self, key, category, desc):
        app = App.get_running_app()
        data = app.data.setdefault("checklist_items", {})
        old = data.get(key, {})
        if isinstance(old, bool):
            old = {"done": old, "responsible": "", "notes": ""}
        box = BoxLayout(orientation="vertical", padding=dp(12), spacing=dp(8))
        box.add_widget(Label(text=category, color=GREEN, bold=True, font_size=dp(16), size_hint_y=None, height=dp(28)))
        box.add_widget(Label(text=desc, color=TEXT, font_size=dp(11), size_hint_y=None, height=dp(48)))
        responsible = SCInput(hint_text="Responsable", text=old.get("responsible", ""), multiline=False)
        notes = SCInput(hint_text="Note / verification", text=old.get("notes", ""), multiline=True)
        status = Spinner(text="TERMINE" if old.get("done", False) else "A VERIFIER",
                         values=("A VERIFIER", "TERMINE", "PROBLEME"),
                         size_hint_y=None, height=dp(48), background_normal="", background_color=LIGHTBLUE, color=TEXT)
        box.add_widget(responsible); box.add_widget(notes); box.add_widget(status)
        save = SCButton(text=app.t("save"), bg=GREEN, size_hint_y=None, height=dp(48))
        box.add_widget(save)
        p = Popup(title=app.t(key), content=box, size_hint=(.94, .78), auto_dismiss=False)
        def do_save(_):
            data[key] = {
                "done": status.text == "TERMINE",
                "problem": status.text == "PROBLEME",
                "responsible": responsible.text.strip(),
                "notes": notes.text.strip(),
                "updated": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            save_data(app.data)
            p.dismiss()
            self.on_pre_enter()
        save.bind(on_release=do_save)
        p.open()

    def save(self, *_):
        app = App.get_running_app()
        data = app.data.setdefault("checklist_items", {})
        for key, cb in self.rows.items():
            old = data.get(key, {})
            if isinstance(old, bool):
                old = {"done": old, "responsible": "", "notes": ""}
            old["done"] = bool(cb.active)
            old["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            data[key] = old
        save_data(app.data)
        popup(app.t("checklist"), "Checklist depart enregistree")

    def reset_all(self, *_):
        app = App.get_running_app()
        for key, _, _ in self.ITEMS:
            app.data.setdefault("checklist_items", {})[key] = {"done": False, "responsible": "", "notes": ""}
        save_data(app.data)
        self.on_pre_enter()


class StockScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app(); root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8)); root.add_widget(Header(app.t("stock"))); b=SCButton(text="+  "+app.t("add_stock"),bg=PURPLE); b.bind(on_release=self.add); root.add_widget(b); sv=ScrollView(do_scroll_x=False); self.lst=GridLayout(cols=1,spacing=dp(8),size_hint_y=None); self.lst.bind(minimum_height=self.lst.setter("height")); sv.add_widget(self.lst); root.add_widget(sv); self.add_widget(root); self.refresh()
    def refresh(self):
        app=App.get_running_app(); self.lst.clear_widgets()
        for i,s in enumerate(app.data.get("stock",[])):
            low=int(s.get("quantity",0))<=int(s.get("minimum",0)); c=Card(orientation="horizontal",bg=LIGHTRED if low else LIGHTGREEN,size_hint_y=None,height=dp(78)); c.add_widget(Label(text=s.get("item","")+"\n"+app.t("quantity")+": "+str(s.get("quantity",0))+" / "+str(s.get("minimum",0)),color=RED if low else GREEN,font_size=dp(11))); d=SCButton(text=app.t("delete"),bg=RED,height=dp(40)); d.size_hint_x=None; d.width=dp(82); d.bind(on_release=lambda _,x=i:self.remove(x)); c.add_widget(d); self.lst.add_widget(c)
        if not app.data.get("stock"): self.lst.add_widget(Label(text=app.t("no_data"),color=MUTED,size_hint_y=None,height=dp(60)))
    def add(self,*_):
        app=App.get_running_app(); box=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(7)); item=SCInput(hint_text=app.t("item"),multiline=False); qty=SCInput(hint_text=app.t("quantity"),multiline=False,input_filter="int"); minimum=SCInput(hint_text=app.t("minimum"),multiline=False,input_filter="int"); save=SCButton(text=app.t("save"),bg=GREEN); [box.add_widget(x) for x in (item,qty,minimum,save)]; p=Popup(title=app.t("add_stock"),content=box,size_hint=(.9,.58))
        def go(_):
            if item.text.strip(): app.data.setdefault("stock",[]).append({"item":item.text.strip(),"quantity":int(qty.text or 0),"minimum":int(minimum.text or 0)}); save_data(app.data); p.dismiss(); self.refresh()
        save.bind(on_release=go); p.open()
    def remove(self,i):
        app=App.get_running_app();
        if 0<=i<len(app.data.get("stock",[])): app.data["stock"].pop(i); save_data(app.data); self.refresh()


class BroadcastScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets(); app=App.get_running_app(); root=BoxLayout(orientation="vertical",padding=dp(10),spacing=dp(8)); root.add_widget(Header(app.t("broadcast"))); self.message=SCInput(hint_text=app.t("message"),multiline=True,size_hint_y=None,height=dp(150)); root.add_widget(self.message); b=SCButton(text=app.t("send_message"),bg=ORANGE); b.bind(on_release=self.send); root.add_widget(b); root.add_widget(Label(text=(app.data.get("server") or app.t("not_connected")),color=MUTED,font_size=dp(10))); self.add_widget(root)
    def send(self,*_):
        app=App.get_running_app(); msg=self.message.text.strip()
        if not msg: return
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"); payload={"title":app.t("broadcast"),"message":msg,"date":now,"ts":int(time.time())}; app.data.setdefault("broadcasts",[]).insert(0,payload); app.data.setdefault("notifications",[]).insert(0,payload); save_data(app.data); local_notify("SMART CARAVAN",msg); base=server_base(app.data.get("server",""));
        if base: threading.Thread(target=post_server_notification,args=(base,payload),daemon=True).start()
        self.message.text=""; popup(app.t("broadcast"),app.t("saved"))


# ============================================================
# APP
# ============================================================

class SmartCaravan(App):
    def build(self):
        self.title = "SMART CARAVAN"
        self.data = load_data()
        self.role = "member"
        self._server_since = 0

        self.sm = ScreenManager(
            transition=FadeTransition(duration=.12)
        )
        self.build_screens()
        self.sm.current = "dashboard"
        Window.bind(on_keyboard=self.on_keyboard)
        return self.sm

    def on_start(self):
        self._server_since = int(time.time())
        self.request_notification_permission()
        Clock.schedule_interval(self.poll_server, 5)

    def request_notification_permission(self):
        # Android 13+ requires runtime notification permission. On Pydroid or
        # older Android versions this safely does nothing.
        try:
            from android.permissions import request_permissions, Permission
            perms = []
            if hasattr(Permission, "POST_NOTIFICATIONS"):
                perms.append(Permission.POST_NOTIFICATIONS)
            if perms:
                request_permissions(perms)
        except Exception:
            pass

    def poll_server(self, _dt):
        base=server_base(self.data.get("server", ""))
        if not base: return
        since=getattr(self, "_server_since", 0)
        def worker():
            try:
                items=fetch_server_notifications(base, since)
            except Exception:
                return
            if not items: return
            def apply(_dt):
                newest=since
                for n in items:
                    self.data.setdefault("notifications", []).insert(0, n)
                    local_notify(n.get("title", "SMART CARAVAN"), n.get("message", ""))
                    try: newest=max(newest, int(n.get("ts", newest)))
                    except Exception: pass
                self._server_since=newest
                save_data(self.data)
                if self.sm.current=="notifications": self.sm.get_screen("notifications").refresh()
            Clock.schedule_once(apply, 0)
        threading.Thread(target=worker, daemon=True).start()

    def go_to(self, target):
        if target not in self.sm.screen_names:
            popup("Navigation", "Screen not found: " + str(target))
            return
        try:
            self.sm.transition = NoTransition()
            self.sm.current = target
        except Exception as e:
            popup("Navigation error", str(e))

    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        # Android back: return to dashboard instead of closing the app.
        if key in (27, 4):
            if self.sm.current != "dashboard":
                self.go_to("dashboard")
                return True
        return False

    def lang(self):
        return self.data.get("language", "fr")

    def t(self, key):
        return T[self.lang()].get(key, EXTRA_T.get(self.lang(), {}).get(key, key))

    def build_screens(self):
        self.sm.clear_widgets()

        # No login screen: the application opens directly on the dashboard.
        self.sm.add_widget(DashboardScreen(name="dashboard"))
        self.sm.add_widget(DangerScreen(name="danger"))
        self.sm.add_widget(ParticipantsScreen(name="participants"))
        self.sm.add_widget(HealthScreen(name="health"))
        self.sm.add_widget(NotificationsScreen(name="notifications"))
        self.sm.add_widget(ReportsScreen(name="reports"))
        self.sm.add_widget(SettingsScreen(name="settings"))
        self.sm.add_widget(VehiclesScreen(name="vehicles"))
        self.sm.add_widget(EventsScreen(name="events"))
        self.sm.add_widget(ContactsScreen(name="contacts"))
        self.sm.add_widget(TeamScreen(name="team"))
        self.sm.add_widget(OperationsScreen(name="operations"))
        self.sm.add_widget(TasksScreen(name="tasks"))
        self.sm.add_widget(ChecklistScreen(name="checklist"))
        self.sm.add_widget(StockScreen(name="stock"))
        self.sm.add_widget(BroadcastScreen(name="broadcast"))
        self.sm.add_widget(ProfileScreen(name="profile"))
        self.sm.add_widget(SOSScreen(name="sos"))

        if self.sm.current not in (
            "dashboard", "danger",
            "participants", "health", "notifications",
            "reports", "settings", "vehicles", "events", "contacts", "team", "operations", "tasks", "checklist", "stock", "broadcast", "profile", "sos"
        ):
            self.sm.current = "dashboard"


if __name__ == "__main__":
    SmartCaravan().run()
