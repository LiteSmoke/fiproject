
<template>
  <div>
    <h1>My FI</h1>
    <ul class="nav nav-tabs" id="myTabs" role="tablist">
      <li class="nav-item" role="presentation">
        <button
          class="nav-link active"
          id="transactions-tab"
          data-bs-toggle="tab"
          data-bs-target="#transactions"
          type="button"
          role="tab"
          aria-controls="transactions"
          aria-selected="true"
        >
          Transactions
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="admin-tab"
          data-bs-toggle="tab"
          data-bs-target="#admin"
          type="button"
          role="tab"
          aria-controls="admin"
          aria-selected="false"
        >
          Admin
        </button>
      </li>
    </ul>
    <div class="tab-content" id="myTabsContent">
      <div
        class="tab-pane fade show active"
        id="transactions"
        role="tabpanel"
        aria-labelledby="transactions-tab"
      >
        <TransactionsList></TransactionsList>
      </div>
      <div
        class="tab-pane fade"
        id="admin"
        role="tabpanel"
        aria-labelledby="admin-tab"
      >
        <!-- Your Admin component goes here -->
        <AdminMain></AdminMain>
      </div>
    </div>
  </div>
</template>

<script>

import TransactionsList from './components/TransactionsList.vue';
import AdminMain from './components/Admin/AdminMain.vue';

export default {
  components: {
    TransactionsList,
    AdminMain,
  },
};
</script>
