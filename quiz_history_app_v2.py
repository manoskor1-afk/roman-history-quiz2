
import streamlit as st

st.set_page_config(page_title="Ιστορία Ε’ - Ρωμαϊκή Εποχή (Quiz)", page_icon="🏛️", layout="centered")

st.title("🏛️ Ιστορία Ε’ Δημοτικού – Ρωμαϊκή Εποχή")
st.write("Επίλεξε μάθημα και απάντησε στις ερωτήσεις. Πάρε άμεση ανατροφοδότηση για κάθε απάντηση!")

LESSONS = {
    "Η κατάκτηση της Ελλάδας από τους Ρωμαίους": [
        {"type": "mc", "q": "Πότε κατέκτησαν οι Ρωμαίοι την Ελλάδα;", "options": ["189 π.Χ.", "198 π.Χ.", "146 π.Χ.", "120 π.Χ."], "answer": "146 π.Χ."},
        {"type": "mc", "q": "Ποιο ήταν το σχέδιο των Ρωμαίων για να κυβερνούν ευκολότερα τους Έλληνες;", "options": ["Διαίρει και βασίλευε", "Ελευθερία και φιλία", "Συμμαχία και ανεξαρτησία", "Νόμοι και ισότητα"], "answer": "Διαίρει και βασίλευε"},
        {"type": "tf", "q": "Οι Ρωμαίοι φέρθηκαν σκληρά στις πόλεις που αντιστάθηκαν.", "answer": True},
        {"type": "tf", "q": "Οι Ρωμαίοι άφησαν ανεξάρτητες τις πόλεις που δεν αντιστάθηκαν.", "answer": True},
        {"type": "mc", "q": "Τι έκαναν οι Ρωμαίοι στις πόλεις που αντιστάθηκαν;", "options": ["Τις άφησαν ελεύθερες", "Έβαλαν φόρους και φρουρές", "Τις βοήθησαν οικονομικά", "Έδωσαν γη στους κατοίκους"], "answer": "Έβαλαν φόρους και φρουρές"},
        {"type": "mc", "q": "Πώς αισθάνονταν οι Έλληνες για τη ρωμαϊκή κυριαρχία;", "options": ["Χαρούμενοι", "Αδιάφοροι", "Δυσαρεστημένοι", "Υπερήφανοι"], "answer": "Δυσαρεστημένοι"},
        {"type": "tf", "q": "Οι Ρωμαίοι δυσκολεύονταν να διοικήσουν τις πολλές ελληνικές πόλεις.", "answer": True},
    ],
    "Οι Ρωμαίοι γνωρίζουν τον ελληνικό πολιτισμό": [
        {"type": "mc", "q": "Τι γνώρισαν οι Ρωμαίοι με την κατάκτηση της Ελλάδας;", "options": ["Τον ελληνικό πολιτισμό", "Τις ελληνικές μάχες", "Τις πηγές του Νείλου", "Την Περσική Αυτοκρατορία"], "answer": "Τον ελληνικό πολιτισμό"},
        {"type": "tf", "q": "Οι Ρωμαίοι θαύμασαν τους ναούς και τα αγάλματα των Ελλήνων.", "answer": True},
        {"type": "mc", "q": "Ποια γλώσσα έμαθαν πολλοί Ρωμαίοι;", "options": ["Αιγυπτιακά", "Ελληνικά", "Λατινικά", "Περσικά"], "answer": "Ελληνικά"},
        {"type": "tf", "q": "Οι Ρωμαίοι έπαιζαν ελληνικές τραγωδίες και κωμωδίες στα θέατρά τους.", "answer": True},
        {"type": "mc", "q": "Ποιο ήταν το αποτέλεσμα της συνεργασίας Ελλήνων και Ρωμαίων;", "options": ["Νέος πολιτισμός – Ελληνορωμαϊκός", "Διαίρεση", "Κατάργηση της Ρώμης", "Νέος πόλεμος"], "answer": "Νέος πολιτισμός – Ελληνορωμαϊκός"},
        {"type": "tf", "q": "Οι Ρωμαίοι δεν εκτίμησαν την ελληνική τέχνη.", "answer": False},
        {"type": "mc", "q": "Ποιοι Ρωμαίοι στόλιζαν την Αθήνα με έργα;", "options": ["Φιλέλληνες άρχοντες", "Αιχμάλωτοι", "Δούλοι", "Γεωργοί"], "answer": "Φιλέλληνες άρχοντες"},
    ],
    "Η ρωμαϊκή αυτοκρατορία και η διοίκησή της": [
        {"type": "tf", "q": "Οι Ρωμαίοι ονόμαζαν τη Μεσόγειο 'η θάλασσά μας' (mare nostrum).", "answer": True},
        {"type": "mc", "q": "Πόσος ήταν περίπου ο πληθυσμός της ρωμαϊκής αυτοκρατορίας;", "options": ["5 εκατομμύρια", "20 εκατομμύρια", "50 εκατομμύρια", "100 εκατομμύρια"], "answer": "50 εκατομμύρια"},
        {"type": "mc", "q": "Ποιος ήταν ο 'πρώτος πολίτης' της αυτοκρατορίας;", "options": ["Ο αυτοκράτορας", "Ο στρατηγός", "Ο ύπατος", "Ο συγκλητικός"], "answer": "Ο αυτοκράτορας"},
        {"type": "tf", "q": "Οι Ρωμαίοι ψήφισαν δικαιότερους νόμους και φρόντιζαν να τηρούνται.", "answer": True},
        {"type": "mc", "q": "Ποιο ήταν το αποτέλεσμα των μέτρων διακυβέρνησης;", "options": ["Αναρχία", "Ρωμαϊκή ειρήνη", "Πόλεμος", "Επανάσταση"], "answer": "Ρωμαϊκή ειρήνη"},
        {"type": "tf", "q": "Η ρωμαϊκή ειρήνη κράτησε περίπου 200 χρόνια.", "answer": True},
        {"type": "mc", "q": "Ποιοι τοπικοί άρχοντες επέβλεπαν τις επαρχίες;", "options": ["Ανθύπατοι", "Ύπατοι", "Φρουροί", "Πρέσβεις"], "answer": "Ανθύπατοι"},
    ],
    "Η ζωή στη Ρώμη και στην ύπαιθρο": [
        {"type": "mc", "q": "Πού ήταν χτισμένη η Ρώμη;", "options": ["Δίπλα στον Τίβερη ποταμό", "Στον Νείλο", "Στον Δούναβη", "Στον Τάμεση"], "answer": "Δίπλα στον Τίβερη ποταμό"},
        {"type": "tf", "q": "Η Ρώμη ήταν στολισμένη με ναούς και έργα τέχνης.", "answer": True},
        {"type": "mc", "q": "Ποιος ήταν ο πληθυσμός της Ρώμης στην ακμή;", "options": ["500.000", "1.500.000", "3.000.000", "100.000"], "answer": "1.500.000"},
        {"type": "mc", "q": "Πού ζούσαν οι περισσότεροι φτωχοί κάτοικοι;", "options": ["Σε πολυκατοικίες", "Σε παλάτια", "Σε βίλες", "Σε σκηνές"], "answer": "Σε πολυκατοικίες"},
        {"type": "tf", "q": "Οι κάτοικοι της υπαίθρου ήταν γεωργοί, βοσκοί και τεχνίτες.", "answer": True},
        {"type": "mc", "q": "Ποιοι φρόντιζαν τα αγροκτήματα των μεγάλων γαιοκτημόνων;", "options": ["Δούλοι", "Μισθωτοί", "Πολίτες", "Στρατιώτες"], "answer": "Δούλοι"},
        {"type": "mc", "q": "Πού πήγαιναν πλούσιοι και φτωχοί για διασκέδαση;", "options": ["Στις γιορτές και στους αγώνες", "Στο θέατρο μόνο", "Στο παλάτι", "Στη Σύγκλητο"], "answer": "Στις γιορτές και στους αγώνες"},
    ],
}

if "lesson" not in st.session_state: st.session_state.lesson = None
if "q_idx" not in st.session_state: st.session_state.q_idx = 0
if "score" not in st.session_state: st.session_state.score = 0
if "answered" not in st.session_state: st.session_state.answered = False

st.subheader("Επίλεξε Μάθημα")
cols = st.columns(2)
lesson_names = list(LESSONS.keys())
for i, name in enumerate(lesson_names):
    if cols[i%2].button(name, use_container_width=True):
        st.session_state.lesson = name
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.session_state.answered = False

st.markdown("---")

if st.session_state.lesson is None:
    st.info("Επίλεξε ένα μάθημα για να ξεκινήσεις.")
    st.stop()

questions = LESSONS[st.session_state.lesson]
total = len(questions)
q = questions[st.session_state.q_idx]

st.write(f"**{st.session_state.lesson}** – Ερώτηση {st.session_state.q_idx+1} από {total}")

if q["type"] == "mc":
    user = st.radio("Επίλεξε:", q["options"], index=None, key=f"q{st.session_state.q_idx}")
    if st.button("Υποβολή απάντησης", type="primary"):
        if user == q["answer"]:
            st.success("✅ Σωστά!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Λάθος. Η σωστή απάντηση είναι: {q['answer']}")
        st.session_state.answered = True
elif q["type"] == "tf":
    user = st.radio("Είναι σωστό ή λάθος;", ["Σωστό", "Λάθος"], index=None, key=f"q{st.session_state.q_idx}")
    if st.button("Υποβολή απάντησης", type="primary"):
        correct = "Σωστό" if q["answer"] else "Λάθος"
        if user == correct:
            st.success("✅ Σωστά!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Λάθος. Η σωστή απάντηση είναι: {correct}")
        st.session_state.answered = True

if st.session_state.answered:
    if st.session_state.q_idx + 1 < total:
        if st.button("Επόμενη ➜"):
            st.session_state.q_idx += 1
            st.session_state.answered = False
    else:
        st.markdown("---")
        st.success(f"Ολοκλήρωσες το μάθημα! Σκορ: {st.session_state.score}/{total}")
        if st.button("Ξεκίνησε ξανά"):
            st.session_state.q_idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
        if st.button("Επίλεξε άλλο μάθημα"):
            st.session_state.lesson = None
