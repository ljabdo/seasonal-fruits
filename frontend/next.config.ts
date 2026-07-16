import type { NextConfig } from "next";

// Produce photos are bundled under public/produce/ and served same-origin, so no
// remote image hosts are configured.
const nextConfig: NextConfig = {
  output: "standalone",
};

export default nextConfig;
