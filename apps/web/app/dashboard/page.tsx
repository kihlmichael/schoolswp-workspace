import { redirect } from "next/navigation";
import { createInsForgeServerClient } from "@/lib/insforge-server";
import { Button } from "@/components/ui/button";

export default async function DashboardPage() {
  const insforge = await createInsForgeServerClient();
  const { data, error } = await insforge.auth.getCurrentUser();

  if (error || !data?.user) {
    redirect("/login");
  }

  return (
    <main className="flex min-h-svh flex-col items-center justify-center gap-6 p-4">
      <div className="text-center">
        <h1 className="text-2xl font-semibold">Tableau de bord</h1>
        <p className="text-muted-foreground">
          Connecte en tant que {data.user.email}
        </p>
      </div>
      <form action="/api/auth/sign-out" method="post">
        <Button type="submit" variant="outline">
          Se deconnecter
        </Button>
      </form>
    </main>
  );
}
