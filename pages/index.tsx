import { useState, useEffect } from 'react';
import { supabase } from '../utils/supabaseClient';
import AuthComponent from '../components/Auth';
import Dashboard from '../components/Dashboard';

export default function Home() {
  const [session, setSession] = useState(null);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session);
    });

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session);
    });

    return () => subscription.unsubscribe();
  }, []);

  if (!session) {
    return <AuthComponent />;
  } else {
    return <Dashboard session={session} />;
  }
}