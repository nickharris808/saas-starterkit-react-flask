import React, { useEffect, useState } from 'react';
import { useAuth } from '../hooks/useAuth';
import { useSupabase } from '../hooks/useSupabase';

const Dashboard = () => {
  const { user } = useAuth();
  const supabase = useSupabase();
  const [profile, setProfile] = useState(null);
  const [subscriptionStatus, setSubscriptionStatus] = useState(null);

  useEffect(() => {
    const fetchProfileAndSubscription = async () => {
      try {
        // Fetch user profile
        const { data: profileData, error: profileError } = await supabase
          .from('profiles')
          .select('*')
          .eq('user_id', user.id)
          .single();

        if (profileError) throw profileError;
        setProfile(profileData);

        // Fetch subscription status
        const { data: subscriptionData, error: subscriptionError } = await supabase
          .from('subscriptions')
          .select('status')
          .eq('user_id', user.id)
          .single();

        if (subscriptionError) throw subscriptionError;
        setSubscriptionStatus(subscriptionData?.status || 'No active subscription');

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    if (user) {
      fetchProfileAndSubscription();
    }
  }, [user, supabase]);

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Welcome to your Dashboard</h1>
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <h2 className="text-xl font-semibold mb-2">Profile Information</h2>
        <p><strong>Name:</strong> {profile.first_name} {profile.last_name}</p>
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>Subscription Status:</strong> {subscriptionStatus}</p>
      </div>
      {/* Add more dashboard widgets or components here */}
    </div>
  );
};

export default Dashboard;