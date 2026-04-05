const recommendations = [
  "Abre con una pregunta provocadora en los primeros 2 segundos.",
  "Introduce prueba social (caso real o cifra) antes del segundo 8.",
  "Cierra con CTA único y claro para mejorar conversiones.",
  "Reutiliza formato top performer para tu nicho B2B."
];

export function Recommendations() {
  return (
    <section className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold">Sugerencias virales con IA</h2>
      <ul className="mt-3 list-disc space-y-2 pl-5 text-sm text-slate-700">
        {recommendations.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}
