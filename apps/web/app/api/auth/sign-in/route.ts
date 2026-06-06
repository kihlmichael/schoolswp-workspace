import { NextResponse } from "next/server";
import { createServerClient, setAuthCookies } from "@insforge/sdk/ssr";

export async function POST(request: Request) {
  const client = createServerClient();
  const { data, error } = await client.auth.signInWithPassword(
    await request.json(),
  );

  if (error || !data?.accessToken) {
    return Response.json(
      {
        error: error?.error ?? "AUTH_UNAUTHORIZED",
        message: error?.message ?? "Sign in failed",
      },
      { status: error?.statusCode ?? 401 },
    );
  }

  const response = NextResponse.json({ user: data.user });
  setAuthCookies(response.cookies, {
    accessToken: data.accessToken,
    refreshToken: data.refreshToken,
  });

  return response;
}
