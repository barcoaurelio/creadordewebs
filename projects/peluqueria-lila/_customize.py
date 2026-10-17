import io

path = "index.html"
html = io.open(path, encoding="utf-8").read()

reps = [
    # ---------- HEAD ----------
    ('<html lang="en"', '<html lang="es"'),
    ('<title>Willow &amp; Sage | Salon and Day Spa</title>',
     '<title>Lila Peluquería | Peluquería y estética en Rosario</title>'),
    ('<meta name="description" content="Willow &amp; Sage is a calm, unhurried salon and day spa. Hair, skin, nails and massage by appointment. Book online or call us.">',
     '<meta name="description" content="Lila Peluquería es un salón tranquilo y sin prisa en Rosario. Corte, color, barbería, estética y spa con cita. Reservá online o llamá al 341 555-0188.">'),
    # ---------- NAV ----------
    ('<a href="#top" class="font-display text-2xl italic tracking-wide">Willow &amp; Sage</a>',
     '<a href="#top" class="font-display text-2xl italic tracking-wide">Lila Peluquería</a>'),
    # ---------- HERO ----------
    ('<p class="text-xs uppercase tracking-widest2 text-clay">Salon &middot; Skin &middot; Spa</p>',
     '<p class="text-xs uppercase tracking-widest2 text-clay">Peluquería &middot; Estética &middot; Spa</p>'),
    ('        An unhurried hour,<br><em>entirely yours.</em>',
     '        Una hora sin apuro,<br><em>enteramente tuya.</em>'),
    ('        Willow &amp; Sage is a quiet studio for hair, skin and rest. No double-booking,\n        no rushing, no hard sell at the register. Just careful work by people who love it.',
     '        Lila Peluquería es un estudio silencioso para el cabello, la piel y el descanso.\n        Sin doble reserva, sin apuro, sin venderte nada al mostrador. Solo trabajo cuidado\n        por gente que lo hace con ganas.'),
    # ---------- INTRO BAND ----------
    ('        &ldquo;We book fewer appointments on purpose. Your hour is yours, from the first\n        consultation to the last cup of tea.&rdquo;',
     '        &ldquo;Reservamos menos citas a propósito. Tu hora es tuya, desde la primera\n        consulta hasta el último mate.&rdquo;'),
    ('Amara Chen, Founder', 'Lucía Fernández, Fundadora'),
    # ---------- SERVICES HEADING ----------
    ('<p class="text-xs uppercase tracking-widest2 text-clay">Menu of Services</p>',
     '<p class="text-xs uppercase tracking-widest2 text-clay">Nuestros servicios</p>'),
    ('<h2 class="mt-4 font-display text-4xl font-medium md:text-5xl">Services &amp; Pricing</h2>',
     '<h2 class="mt-4 font-display text-4xl font-medium md:text-5xl">Servicios y precios</h2>'),
    ('<p class="mx-auto mt-4 max-w-md text-sm text-stone">All appointments begin with a short consultation. Prices are starting points and confirmed before we begin.</p>',
     '<p class="mx-auto mt-4 max-w-md text-sm text-stone">Toda cita empieza con una consulta breve. Los precios son desde y se confirman antes de empezar.</p>'),
    # ---------- COLUMN: HAIR ----------
    ('<h3 class="border-b border-clay pb-3 font-display text-2xl italic">Hair</h3>',
     '<h3 class="border-b border-clay pb-3 font-display text-2xl italic">Cabello</h3>'),
    ('<span>Cut &amp; finish</span><span class="leader"></span><span class="font-display text-lg">from 65</span>',
     '<span>Corte y brushing</span><span class="leader"></span><span class="font-display text-lg">desde $28.000</span>'),
    ('<span>Single-process color</span><span class="leader"></span><span class="font-display text-lg">from 95</span>',
     '<span>Color raíz (un tono)</span><span class="leader"></span><span class="font-display text-lg">desde $45.000</span>'),
    ('<span>Balayage / lived-in color</span><span class="leader"></span><span class="font-display text-lg">from 180</span>',
     '<span>Balayage / color a medida</span><span class="leader"></span><span class="font-display text-lg">desde $85.000</span>'),
    ('<span>Deep conditioning ritual</span><span class="leader"></span><span class="font-display text-lg">45</span>',
     '<span>Hidratación profunda</span><span class="leader"></span><span class="font-display text-lg">$22.000</span>'),
    ('<span>Occasion styling</span><span class="leader"></span><span class="font-display text-lg">from 75</span>',
     '<span>Peinado para eventos</span><span class="leader"></span><span class="font-display text-lg">desde $35.000</span>'),
    ('<span>Classic manicure</span><span class="leader"></span><span class="font-display text-lg">40</span>',
     '<span>Manicura clásica</span><span class="leader"></span><span class="font-display text-lg">$15.000</span>'),
    # ---------- COLUMN: SKIN ----------
    ('<h3 class="border-b border-clay pb-3 font-display text-2xl italic">Skin</h3>',
     '<h3 class="border-b border-clay pb-3 font-display text-2xl italic">Estética</h3>'),
    ('<span>Signature facial, 60 min</span><span class="leader"></span><span class="font-display text-lg">110</span>',
     '<span>Limpieza facial, 60 min</span><span class="leader"></span><span class="font-display text-lg">$38.000</span>'),
    ('<span>Calming facial for sensitive skin</span><span class="leader"></span><span class="font-display text-lg">120</span>',
     '<span>Facial calmante, piel sensible</span><span class="leader"></span><span class="font-display text-lg">$42.000</span>'),
    ('<span>Dermaplaning add-on</span><span class="leader"></span><span class="font-display text-lg">40</span>',
     '<span>Dermaplaning (adicional)</span><span class="leader"></span><span class="font-display text-lg">$18.000</span>'),
    ('<span>Brow shaping &amp; tint</span><span class="leader"></span><span class="font-display text-lg">55</span>',
     '<span>Perfilado y tintura de cejas</span><span class="leader"></span><span class="font-display text-lg">$12.000</span>'),
    # ---------- COLUMN: SPA ----------
    ('<span>Swedish massage, 60 min</span><span class="leader"></span><span class="font-display text-lg">105</span>',
     '<span>Masaje descontracturante, 60 min</span><span class="leader"></span><span class="font-display text-lg">$35.000</span>'),
    ('<span>Deep tissue, 60 min</span><span class="leader"></span><span class="font-display text-lg">120</span>',
     '<span>Masaje profundo, 60 min</span><span class="leader"></span><span class="font-display text-lg">$40.000</span>'),
    ('<span>Spa pedicure</span><span class="leader"></span><span class="font-display text-lg">65</span>',
     '<span>Pedicura spa</span><span class="leader"></span><span class="font-display text-lg">$22.000</span>'),
    ('<span>Half-day retreat, 3 hrs</span><span class="leader"></span><span class="font-display text-lg">265</span>',
     '<span>Media jornada de spa, 3 h</span><span class="leader"></span><span class="font-display text-lg">$75.000</span>'),
    # ---------- STUDIO ----------
    ('<p class="text-xs uppercase tracking-widest2 text-clay">The Studio</p>',
     '<p class="text-xs uppercase tracking-widest2 text-clay">El estudio</p>'),
    ('<h2 class="mt-4 font-display text-4xl font-medium leading-tight md:text-5xl">Designed to slow you down</h2>',
     '<h2 class="mt-4 font-display text-4xl font-medium leading-tight md:text-5xl">Diseñado para bajar un cambio</h2>'),
    ('          Soft light, warm towels, and a strict no-phone-calls policy on the spa floor.\n          Every product we use is one we take home ourselves, and we will tell you exactly\n          what we used so you can recreate it, no purchase required.',
     '          Luz suave, toallas tibias y prohibido atender llamadas en la sala de spa.\n          Cada producto que usamos lo tenemos en casa: te decimos exactamente qué usamos\n          para que lo puedas replicar, sin necesidad de comprar nada.'),
    ('<span class="mt-1 h-px w-8 shrink-0 bg-clay"></span>Complimentary tea bar and quiet lounge',
     '<span class="mt-1 h-px w-8 shrink-0 bg-clay"></span>Rincón de mates y sala de espera tranquila'),
    ('<span class="mt-1 h-px w-8 shrink-0 bg-clay"></span>Fragrance-free options for every treatment',
     '<span class="mt-1 h-px w-8 shrink-0 bg-clay"></span>Opciones sin fragancia para cada tratamiento'),
    ('<span class="mt-1 h-px w-8 shrink-0 bg-clay"></span>Accessible entrance and treatment rooms',
     '<span class="mt-1 h-px w-8 shrink-0 bg-clay"></span>Entrada y salas accesibles'),
    # ---------- TEAM ----------
    ('<p class="text-xs uppercase tracking-widest2 text-clay">The Team</p>',
     '<p class="text-xs uppercase tracking-widest2 text-clay">El equipo</p>'),
    ('<h2 class="mt-4 font-display text-4xl font-medium md:text-5xl">In careful hands</h2>',
     '<h2 class="mt-4 font-display text-4xl font-medium md:text-5xl">En buenas manos</h2>'),
    ('<h3 class="mt-5 font-display text-2xl italic">Amara Chen</h3>',
     '<h3 class="mt-5 font-display text-2xl italic">Lucía Fernández</h3>'),
    ('<p class="mt-1 text-xs uppercase tracking-widest2 text-stone">Founder &middot; Color Specialist</p>',
     '<p class="mt-1 text-xs uppercase tracking-widest2 text-stone">Fundadora &middot; Especialista en color</p>'),
    ('<h3 class="mt-5 font-display text-2xl italic">Noor Haddad</h3>',
     '<h3 class="mt-5 font-display text-2xl italic">Sofía Benítez</h3>'),
    ('<p class="mt-1 text-xs uppercase tracking-widest2 text-stone">Lead Esthetician</p>',
     '<p class="mt-1 text-xs uppercase tracking-widest2 text-stone">Esteticista</p>'),
    ('<h3 class="mt-5 font-display text-2xl italic">Elena Petrov</h3>',
     '<h3 class="mt-5 font-display text-2xl italic">Diego Sosa</h3>'),
    ('<p class="mt-1 text-xs uppercase tracking-widest2 text-stone">Massage Therapist, LMT</p>',
     '<p class="mt-1 text-xs uppercase tracking-widest2 text-stone">Barbería y cortes</p>'),
    # ---------- TESTIMONIALS ----------
    (u'&ldquo;First salon where I\'ve never once felt rushed. My balayage has strangers asking for the name of the place.&rdquo;',
     '&ldquo;Primera peluquería donde nunca me apuraron. Mi balayage hace que desconocidos me pregunten el nombre del lugar.&rdquo;'),
    ('Priya S.', 'Carla M.'),
    ('&ldquo;The half-day retreat is the best gift my partner has ever given me. I fell asleep during the facial.&rdquo;',
     '&ldquo;La media jornada de spa es el mejor regalo que me hicieron. Me quedé dormida en la limpieza facial.&rdquo;'),
    ('Danielle R.', 'Vanesa R.'),
    ('&ldquo;They told me exactly which products they used and never pushed me to buy a thing. I bought two anyway.&rdquo;',
     '&ldquo;Me dijeron exactamente qué productos usaron y nunca me empujaron a comprar nada. Igual compré dos.&rdquo;'),
    ('Hannah M.', 'Julieta P.'),
    # ---------- BOOK ----------
    ('<h2 class="fade-up font-display text-4xl font-medium md:text-5xl">Book your visit</h2>',
     '<h2 class="fade-up font-display text-4xl font-medium md:text-5xl">Reservá tu visita</h2>'),
    ('<p class="fade-up mt-5 text-stone">Appointments open six weeks ahead. Evenings fill quickly; weekday mornings are the quietest.</p>',
     '<p class="fade-up mt-5 text-stone">Las citas se abren con seis semanas de anticipación. Los turnos de tarde se llenan rápido; las mañanas de semana son las más tranquilas.</p>'),
    ('<a href="tel:+15550188" class="bg-pine px-10 py-4 text-xs uppercase tracking-widest2 text-linen transition hover:bg-clay">Call (555) 018-8200</a>',
     '<a href="tel:+543415550188" class="bg-pine px-10 py-4 text-xs uppercase tracking-widest2 text-linen transition hover:bg-clay">Llamá al 341 555-0188</a>'),
    ('<a href="mailto:hello@willowandsage.example" class="border border-pine px-10 py-4 text-xs uppercase tracking-widest2 transition hover:border-clay hover:text-clay">Email Us</a>',
     '<a href="mailto:hola@lilapeluqueria.com" class="border border-pine px-10 py-4 text-xs uppercase tracking-widest2 transition hover:border-clay hover:text-clay">Escribinos</a>'),
    ('<p class="fade-up mt-6 text-[11px] uppercase tracking-widest2 text-stone">Or embed your booking link here (Square, Fresha, Vagaro, GlossGenius)</p>',
     '<p class="fade-up mt-6 text-[11px] uppercase tracking-widest2 text-stone">O acá va tu link de reservas (Fresha, Square, Booksy)</p>'),
    ('<p>36 Alder Lane, Suite 2 &middot; Your City, ST 00000</p>',
     '<p>Av. Pellegrini 1234 &middot; Rosario, Santa Fe</p>'),
    ('<p>Tue - Sat, 9am - 7pm &middot; Closed Sun &amp; Mon</p>',
     '<p>Lun a Sáb, 9 a 20 h &middot; Dom cerrado</p>'),
    # ---------- FOOTER ----------
    ('<p class="font-display text-xl italic">Willow &amp; Sage</p>',
     '<p class="font-display text-xl italic">Lila Peluquería</p>'),
    ('<p class="mt-2 text-[11px] uppercase tracking-widest2 text-stone">&copy; 2026 Willow &amp; Sage Salon and Day Spa</p>',
     '<p class="mt-2 text-[11px] uppercase tracking-widest2 text-stone">&copy; 2026 Lila Peluquería &middot; Rosario</p>'),
    # ---------- JSON-LD ----------
    ('    "name": "Willow & Sage Salon and Day Spa",\n    "telephone": "(555) 018-8200",\n    "address": { "@type": "PostalAddress", "streetAddress": "36 Alder Lane, Suite 2", "addressLocality": "Your City" },',
     '    "name": "Lila Peluquería",\n    "telephone": "+54 341 555-0188",\n    "address": { "@type": "PostalAddress", "streetAddress": "Av. Pellegrini 1234", "addressLocality": "Rosario", "addressRegion": "Santa Fe", "addressCountry": "AR" },'),
]

missing = []
for a, b in reps:
    if a not in html:
        missing.append(a[:70])
    html = html.replace(a, b)

io.open(path, "w", encoding="utf-8", newline="\n").write(html)

print("Reemplazos aplicados: %d/%d" % (len(reps) - len(missing), len(reps)))
if missing:
    print("NO ENCONTRADOS (%d):" % len(missing))
    for m in missing:
        print("  -", m)

leftovers = []
for bad in ["Willow", "Amara Chen", "Noor Haddad", "Elena Petrov", "Your City", "Alder Lane", "willowandsage", "018-8200"]:
    if bad in html:
        leftovers.append(bad)
print("Restos de plantilla:", leftovers if leftovers else "NINGUNO")
