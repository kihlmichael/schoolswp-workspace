import { NextResponse, type NextRequest } from "next/server";
import { updateSession, type CookieStore } from "@insforge/sdk/ssr";

// Next.js 16 renamed middleware.ts -> proxy.ts. Refresh the InsForge session
// before Server Components render so they see fresh auth cookies.
export async function proxy(request: NextRequest) {
  const response = NextResponse.next({ request });

  // Next's Request/ResponseCookies are structurally cookie stores, but their
  // set() overloads differ nominally from the SDK's CookieStore. Pass the real
  // objects (runtime-correct) and bridge the type gap.
  await updateSession({
    requestCookies: request.cookies as unknown as CookieStore,
    responseCookies: response.cookies as unknown as CookieStore,
  });

  return response;
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
