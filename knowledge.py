# Adnovaa Assistant — knowledge base built ONLY from live adnovaa.com facts.
# Site language is English; greetings/fallbacks/handoff prompts are localized.

SITE = "https://adnovaa.com"

LOCAL = {
    "en": {
        "greeting": "Hi! I'm the Adnovaa Assistant. Ask me about buying, paying with USDT, selling, escrow, or your orders.",
        "fallback": "I don't have an answer for that yet. You can rephrase, or tap \"Talk to a human\" and our team will reply by email.",
        "handoff": "Sure — please share your name, email and a short description of the issue, and our team will get back to you.",
        "human_words": ["human", "agent", "person", "support team", "talk to someone"],
    },
    "bn": {
        "greeting": "হ্যালো! আমি Adnovaa Assistant। কেনা, USDT পেমেন্ট, বিক্রি, escrow বা অর্ডার নিয়ে জিজ্ঞেস করুন। (Answers are in English, as on our site.)",
        "fallback": "দুঃখিত, এটার উত্তর এখনো আমার কাছে নেই। \"Talk to a human\" চাপলে আমাদের টিম ইমেইলে উত্তর দেবে।",
        "handoff": "অবশ্যই — আপনার নাম, ইমেইল আর সমস্যাটা ছোট করে লিখুন, আমাদের টিম উত্তর দেবে।",
        "human_words": ["মানুষ", "হিউম্যান", "এজেন্ট"],
    },
    "hi": {
        "greeting": "नमस्ते! मैं Adnovaa Assistant हूँ। खरीदारी, USDT भुगतान, बिक्री, escrow या अपने ऑर्डर के बारे में पूछें। (Answers are in English, as on our site.)",
        "fallback": "माफ़ करें, इसका उत्तर मेरे पास अभी नहीं है। \"Talk to a human\" दबाएँ, हमारी टीम ईमेल से जवाब देगी।",
        "handoff": "ज़रूर — अपना नाम, ईमेल और समस्या का छोटा विवरण दें, हमारी टीम जवाब देगी।",
        "human_words": ["इंसान", "एजेंट", "मानव"],
    },
    "es": {
        "greeting": "¡Hola! Soy el Asistente de Adnovaa. Pregúntame sobre compras, pagos con USDT, ventas, escrow o tus pedidos. (Answers are in English, as on our site.)",
        "fallback": "Lo siento, aún no tengo respuesta para eso. Toca \"Talk to a human\" y nuestro equipo te responderá por correo.",
        "handoff": "Claro — comparte tu nombre, correo y una breve descripción del problema, y nuestro equipo te responderá.",
        "human_words": ["humano", "agente", "persona"],
    },
    "ar": {
        "greeting": "مرحبًا! أنا مساعد Adnovaa. اسألني عن الشراء أو الدفع بـ USDT أو البيع أو الضمان (escrow) أو طلباتك. (Answers are in English, as on our site.)",
        "fallback": "عذرًا، ليس لدي إجابة عن ذلك بعد. اضغط \"Talk to a human\" وسيرد فريقنا عبر البريد الإلكتروني.",
        "handoff": "بالتأكيد — شارك اسمك وبريدك ووصفًا قصيرًا للمشكلة، وسيتواصل معك فريقنا.",
        "human_words": ["إنسان", "موظف", "شخص"],
    },
    "fr": {
        "greeting": "Bonjour ! Je suis l'Assistant Adnovaa. Posez-moi vos questions sur les achats, les paiements en USDT, la vente, l'escrow ou vos commandes. (Answers are in English, as on our site.)",
        "fallback": "Désolé, je n'ai pas encore de réponse. Touchez « Talk to a human » et notre équipe vous répondra par e-mail.",
        "handoff": "Bien sûr — indiquez votre nom, votre e-mail et une courte description du problème, notre équipe vous répondra.",
        "human_words": ["humain", "agent", "personne"],
    },
    "de": {
        "greeting": "Hallo! Ich bin der Adnovaa Assistant. Fragen Sie mich zu Kauf, USDT-Zahlung, Verkauf, Escrow oder Ihren Bestellungen. (Answers are in English, as on our site.)",
        "fallback": "Entschuldigung, dazu habe ich noch keine Antwort. Tippen Sie auf \"Talk to a human\", unser Team antwortet per E-Mail.",
        "handoff": "Gerne — nennen Sie Ihren Namen, Ihre E-Mail und eine kurze Beschreibung des Problems, unser Team meldet sich.",
        "human_words": ["mensch", "mitarbeiter", "person"],
    },
    "pt": {
        "greeting": "Olá! Sou o Assistente Adnovaa. Pergunte sobre compras, pagamento com USDT, vendas, escrow ou seus pedidos. (Answers are in English, as on our site.)",
        "fallback": "Desculpe, ainda não tenho resposta para isso. Toque em \"Talk to a human\" e nossa equipe responderá por e-mail.",
        "handoff": "Claro — compartilhe seu nome, e-mail e uma breve descrição do problema, e nossa equipe responderá.",
        "human_words": ["humano", "atendente", "pessoa"],
    },
    "ru": {
        "greeting": "Здравствуйте! Я — ассистент Adnovaa. Спрашивайте о покупках, оплате USDT, продажах, эскроу или ваших заказах. (Answers are in English, as on our site.)",
        "fallback": "Извините, у меня пока нет ответа. Нажмите «Talk to a human», и наша команда ответит по почте.",
        "handoff": "Конечно — укажите имя, e-mail и краткое описание проблемы, и наша команда ответит вам.",
        "human_words": ["человек", "оператор", "сотрудник"],
    },
    "tr": {
        "greeting": "Merhaba! Ben Adnovaa Assistant. Satın alma, USDT ile ödeme, satış, escrow veya siparişleriniz hakkında sorabilirsiniz. (Answers are in English, as on our site.)",
        "fallback": "Üzgünüm, bunun cevabı henüz bende yok. \"Talk to a human\"a dokunun, ekibimiz e-postayla yanıt versin.",
        "handoff": "Elbette — adınızı, e-postanızı ve sorunun kısa açıklamasını paylaşın, ekibimiz size dönsün.",
        "human_words": ["insan", "temsilci", "yetkili"],
    },
    "ur": {
        "greeting": "السلام علیکم! میں Adnovaa Assistant ہوں۔ خریداری، USDT ادائیگی، فروخت، escrow یا اپنے آرڈرز کے بارے میں پوچھیں۔ (Answers are in English, as on our site.)",
        "fallback": "معذرت، اس کا جواب ابھی میرے پاس نہیں۔ \"Talk to a human\" دبائیں، ہماری ٹیم ای میل سے جواب دے گی۔",
        "handoff": "ضرور — اپنا نام، ای میل اور مسئلے کی مختصر تفصیل بتائیں، ہماری ٹیم جواب دے گی۔",
        "human_words": ["انسان", "نمائندہ"],
    },
}

# Each intent: multilingual keyword hints (English + common equivalents) and an
# English answer written from the site's own pages. {site} is interpolated.
INTENTS = [
    {
        "id": "pay_usdt",
        "keywords": ["usdt", "pay", "payment", "checkout", "trc20", "bep20", "erc20", "solana",
                     "tx hash", "transaction hash", "wallet address", "crypto",
                     "পেমেন্ট", "भुगतान", "pago", "paiement", "zahlung", "pagamento", "оплата", "ödeme", "ادائیگی", "دفع"],
        "answer": (
            "Paying on Adnovaa is USDT-only — prices are in USDT from the start, no conversion surprises.\n"
            "1) At checkout, pick a network: TRC20 (recommended), BEP20, ERC20 or SOL.\n"
            "2) Send the exact order amount to the wallet address shown (a QR code is provided).\n"
            "3) Paste your transaction (TX) hash in the checkout form and place the order.\n"
            "4) Your order stays On Hold while our team verifies the payment on the blockchain — then delivery starts.\n"
            "Full guide: {site}/paying-with-usdt-guide/"
        ),
    },
    {
        "id": "escrow",
        "keywords": ["escrow", "buyer protection", "safe", "scam", "trust", "protect", "confirm receipt",
                     "auto release", "release my money", "নিরাপদ", "सुरक्षित", "seguro", "sicher", "безопасно", "güvenli", "محفوظ"],
        "answer": (
            "Every Adnovaa order is protected by escrow. You pay Adnovaa — not the seller directly. "
            "For digital products, delivery is marked as soon as your payment is verified. You then check the delivery and "
            "confirm receipt from your order page; if you do nothing, the order auto-confirms after 7 days and the seller is paid. "
            "If something is wrong, open a dispute before confirming — that pauses the release while our team reviews both sides.\n"
            "Details: {site}/escrow-protection-digital-products/ and {site}/buyer-protection-badge/"
        ),
    },
    {
        "id": "refund",
        "keywords": ["refund", "money back", "dispute", "problem with order", "not delivered", "wrong product",
                     "রিফান্ড", "वापसी", "reembolso", "remboursement", "rückerstattung", "возврат", "iade", "رقم واپسی", "استرداد"],
        "answer": (
            "If a delivery is missing or not as described, open a dispute from your order page (My Account → Orders) before confirming receipt. "
            "A dispute pauses the escrow release immediately and our team reviews both sides. Unresolved disputes are decided under our Refund Policy, "
            "and approved refunds are returned in USDT.\n"
            "Policy: {site}/refund-policy/ — FAQ: {site}/faq/"
        ),
    },
    {
        "id": "sell",
        "keywords": ["sell", "seller", "vendor", "become a seller", "open a store", "start selling", "commission",
                     "বিক্রি", "विक्रय", "vender", "vendre", "verkaufen", "продавать", "satış", "فروخت", "بيع"],
        "answer": (
            "Selling on Adnovaa is free to start: register, verify your email, and our team approves seller accounts manually. "
            "Then set up your store, enable two-factor authentication (7-day grace period), and add products — each product is reviewed before it goes live. "
            "Commission is 10% on completed sales only; there are no listing fees. Withdrawals start from 10 USDT.\n"
            "Start here: {site}/become-a-seller/ — Seller Academy: {site}/seller-academy/"
        ),
    },
    {
        "id": "withdraw",
        "keywords": ["withdraw", "payout", "cash out", "my earnings", "উত্তোলন", "निकासी", "retiro", "retrait",
                     "auszahlung", "вывод", "çekim", "انخلاء", "سحب"],
        "answer": (
            "Sellers can withdraw earnings from the vendor dashboard (Withdraw) once the balance reaches the 10 USDT minimum, "
            "after the order has completed (buyer confirmed, or the 7-day escrow window passed). Withdrawals are paid in USDT. "
            "For your security, changing a payout wallet locks withdrawals to the new address for 48 hours."
        ),
    },
    {
        "id": "track_order",
        "keywords": ["track", "order status", "where is my order", "my order", "delivery status",
                     "অর্ডার", "आदेश", "pedido", "commande", "bestellung", "заказ", "sipariş", "طلب"],
        "answer": (
            "You can track any order on the Track Order page: {site}/track-order/ — or open My Account → Orders for the full status, "
            "delivery details and the Confirm Receipt / dispute buttons."
        ),
    },
    {
        "id": "categories",
        "keywords": ["categor", "what do you sell", "products", "services", "ad accounts", "gift card", "credit line",
                     "ক্যাটাগরি", "श्रेणी", "categoría", "catégorie", "kategorie", "категория", "kategori", "قسم"],
        "answer": (
            "Adnovaa has 75 categories across 11 groups: Ad Accounts, Ad Funding, Credit Line, Gift Cards & Vouchers, "
            "Tracking & Technical Support, Ads Management, Agency Support, Ad Creatives & Content, Websites & Funnels, "
            "SEO & Marketing Services, and Digital Tools & Software. Browse them from the Categories menu on {site}/ — "
            "or tell me a product name and I'll look it up for you."
        ),
    },
    {
        "id": "coupon",
        "keywords": ["coupon", "discount", "promo", "offer", "launch10", "sale", "কুপন", "छूट", "descuento",
                     "réduction", "rabatt", "скидка", "indirim", "خصم"],
        "answer": (
            "Our launch offer is live: code LAUNCH10 gives 10% off orders of 20 USDT or more — once per customer, until December 31, 2026. "
            "Enter it at checkout. See the Launch Sale page: {site}/launch-sale/ — Adnovaa Plus members save an extra 5% on every order."
        ),
    },
    {
        "id": "plus",
        "keywords": ["adnovaa plus", "plus member", "membership", "সদস্য", "सदस्यता", "membresía", "mitgliedschaft", "üyelik", "عضوية"],
        "answer": (
            "Adnovaa Plus is our buyer membership: 9 USDT for 30 days. Members get an automatic 5% discount on every order, "
            "priority support and a member badge. Join here: {site}/adnovaa-plus/"
        ),
    },
    {
        "id": "credit",
        "keywords": ["buyer credit", "trusted buyer", "pay later", "credit limit", "ঋণ", "उधार", "crédito", "crédit", "kredit", "кредит", "kredi", "قرض"],
        "answer": (
            "Trusted Buyer Credit lets reliable buyers cover part of an order now and settle later. You qualify automatically with 3+ completed orders "
            "and a good buyer rating; the default limit is 50 USDT, usable for up to 30% of a cart. Check your status under My Account → Buyer Credit."
        ),
    },
    {
        "id": "account_verify",
        "keywords": ["verify", "verification", "email not received", "cannot login", "can't login", "kyc", "identity",
                     "যাচাই", "सत्यापन", "verificación", "vérification", "verifizierung", "проверка", "doğrulama", "تحقق"],
        "answer": (
            "New accounts must verify their email before logging in — check your inbox (and spam folder) for the Adnovaa verification email, "
            "or use the resend option on the login page. Sellers can also complete KYC (Seller KYC in the vendor dashboard) to earn the green "
            "KYC Verified badge. Still stuck? Tap \"Talk to a human\" and we'll help."
        ),
    },
    {
        "id": "contact",
        "keywords": ["contact", "email", "address", "company", "where are you", "যোগাযোগ", "संपर्क", "contacto",
                     "kontakt", "контакт", "iletişim", "اتصال"],
        "answer": (
            "You can reach the Adnovaa team at admin@adnovaa.com, through the Contact page {site}/contact/, or with a support ticket in My Account. "
            "Adnovaa, 153 Oak Street, Los Angeles, CA 90001, United States."
        ),
    },
]

QUICK_REPLIES = ["How do I pay with USDT?", "Is buying safe? (escrow)", "How do I sell on Adnovaa?",
                 "Track my order", "Current offers", "Talk to a human"]
