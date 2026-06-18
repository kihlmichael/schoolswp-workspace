import { cookies } from "next/headers";
import { NextResponse } from "next/server";
import { createServerClient } from "@insforge/sdk/ssr";

export async function POST(request: Request) {
  const client = createServerClient({ cookies: await cookies() });
  await client.auth.signOut();

  // 303 turns the form POST into a GET on /login.
  const response = NextResponse.redirect(new URL("/login", request.url), {
    status: 303,
  });
  response.cookies.delete("insforge_access_token");
  response.cookies.delete("insforge_refresh_token");

  return response;
}
