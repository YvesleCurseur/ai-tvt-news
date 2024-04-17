"use client";

import { useState, useEffect } from "react";
import Hero from "@/components/Hero";
import News from "@/components/News";
import Loader from "@/components/Loader";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default function Page() {
  const [data, setData] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  /* A calling the last news */
  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/news`)
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setIsLoading(false);
      });
  }, []);

  return (
    <div>
      <Header />
      <Hero />
      <div className="min-h-[400px]"> {/* Keeping the sapce when loading the news */}
        {isLoading ? (
          <div className="mt-10">
            <Loader />
          </div>
        ) : (
          <News data={data} />
        )}
      </div>
      <Footer />
    </div>
  );
}
