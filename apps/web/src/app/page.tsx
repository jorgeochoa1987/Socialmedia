import { KpiCard } from "@/components/kpi-card";
import { Recommendations } from "@/components/recommendations";
import { UrlLoader } from "@/components/url-loader";

const kpis = [
  { label: "Views totales", value: "1.2M" },
  { label: "Engagement promedio", value: "6.8%" },
  { label: "Retención media", value: "41%" },
  { label: "Crecimiento mensual", value: "+12.4%" }
];

export default function HomePage() {
  return (
    <main className="mx-auto max-w-7xl space-y-6 p-6">
      <header>
        <h1 className="text-3xl font-bold">Dashboard de análisis social</h1>
        <p className="mt-1 text-slate-600">
          KPIs, hooks, retención, oportunidades comerciales y recomendaciones con IA.
        </p>
      </header>

      <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {kpis.map((kpi) => (
          <KpiCard key={kpi.label} {...kpi} />
        ))}
      </section>

      <UrlLoader />
      <Recommendations />
    </main>
  );
}
