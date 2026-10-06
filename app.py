from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import sys

# Set up template folder for both Databricks and Vercel
# Vercel uses /var/task/, Databricks uses regular paths
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'templates')
static_dir = os.path.join(current_dir, 'static')

# Debug: Print available paths (visible in logs)
print(f"[DEBUG] Current dir: {current_dir}", file=sys.stderr)
print(f"[DEBUG] Template dir: {template_dir}", file=sys.stderr)
print(f"[DEBUG] Template dir exists: {os.path.exists(template_dir)}", file=sys.stderr)

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Sample data for Mass schedule
mass_schedule = [
    {
        'title': 'Tamil Mass',
        'date': 'October 18, 2026',
        'day': 'Sunday',
        'time': '4:00 PM',
        'type': 'Tamil Mass',
        'location': 'Paxico, KS',
        'priest': 'TBD',
        'raw_date': '2026-10-18'
    },
    {
        'title': 'Tamil Mass',
        'date': 'November 15, 2026',
        'day': 'Sunday',
        'time': 'TBD',
        'type': 'Tamil Mass',
        'location': 'Holy Trinity Church, Paola, KS',
        'priest': 'TBD',
        'raw_date': '2026-11-15'
    },
    {
        'title': 'Tamil Mass',
        'date': 'December 20, 2026',
        'day': 'Sunday',
        'time': 'TBD',
        'type': 'Tamil Mass',
        'location': 'Holy Trinity Church, Paola, KS',
        'priest': 'TBD',
        'raw_date': '2026-12-20'
    }
]

# Sample events data
events = [
    {
        'title': 'Holy Rosary',
        'date': '2026-10-24',
        'time': 'Saturday',
        'location': 'James Jeneive Home, 13900 Russell Street, #327, Overland Park, KS 66223',
        'description': 'Join us for Holy Rosary prayer at James Jeneive\'s home. All community members are welcome to pray together.',
        'type': 'Prayer Event',
        'contact': 'Contact John for details'
    },
    {
        'title': 'Christmas Program 2026',
        'date': '2026-12-24',
        'time': 'TBD',
        'location': 'Location TBD',
        'description': 'Christmas program is currently in planning stage. Details will be announced soon. Stay tuned for updates!',
        'type': 'Special Event - Planning',
        'contact': 'Contact John for details'
    }
]

# Real photo paths (to be uploaded)
# User will upload: clergy.jpg and mary.jpg to static/images/
clergy_photo = '/static/images/clergy.jpg'
mary_photo = '/static/images/mary.jpg'

# Gallery images
gallery_images = [
    {'url': 'https://i.imgur.com/tu1suNi.jpg', 'title': 'Mother Mary with Our Clergy'},
    {'url': 'https://i.imgur.com/nXLssMU.jpg', 'title': 'Tamil Catholic Community'},
    {'url': 'https://i.imgur.com/oC9jYRr.jpg', 'title': 'Community Gathering'},
    {'url': 'https://i.imgur.com/2dGEWR5.jpg', 'title': 'Mass Celebration'},
    {'url': 'https://i.imgur.com/2FkS2xp.jpg', 'title': 'Community Celebration'},
    {'url': 'https://i.imgur.com/fX2VwCU.jpg', 'title': 'Tamil Mass'},
    {'url': 'https://i.imgur.com/XFZ1nPB.jpg', 'title': 'Faith & Unity'},
    {'url': 'https://i.imgur.com/SPqNdxe.jpg', 'title': 'Community Fellowship'}
]

# Contact information
contact_info = {
    'coordinator': 'John',
    'phone': '(913) 461-2244',
    'whatsapp': '19134612244',
    'email': 'kansastamilcatholic@gmail.com',
    'address': 'Overland Park, KS'
}

@app.route('/')
def index():
    # Get next upcoming Mass
    today = datetime.now().strftime('%Y-%m-%d')
    upcoming_masses = [m for m in mass_schedule if m['raw_date'] >= today]
    next_mass = upcoming_masses[0] if upcoming_masses else None
    
    # Format next mass date and time for display
    if next_mass:
        next_mass_date = next_mass['date']  # Already formatted
        next_mass_time = next_mass['time']
    else:
        next_mass_date = 'TBD'
        next_mass_time = 'TBD'
    
    # Get upcoming events
    upcoming_events = [e for e in events if e['date'] >= today]
    
    # Add icons to events for display
    for event in upcoming_events:
        if 'Rosary' in event['title']:
            event['icon'] = 'hands-praying'
        elif 'Christmas' in event['title']:
            event['icon'] = 'star'
        else:
            event['icon'] = 'calendar-check'
    
    return render_template('index.html',
                         mass_schedule=mass_schedule,
                         masses=mass_schedule,
                         next_mass=next_mass,
                         next_mass_date=next_mass_date,
                         next_mass_time=next_mass_time,
                         events=upcoming_events,
                         gallery=gallery_images,
                         coordinator_name=contact_info['coordinator'],
                         coordinator_phone=contact_info['phone'],
                         whatsapp_link=f"https://wa.me/{contact_info['whatsapp']}",
                         contact=contact_info)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # In production, you'd send an email or save to database
    return jsonify({'success': True, 'message': 'Thank you! We will contact you soon.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)