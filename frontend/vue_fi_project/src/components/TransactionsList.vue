<template>
    <div>
      <h2>Transactions</h2>
      <table class="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Date</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Category</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="t in transactions" :key="t.id">
            <td>{{ t.id }}</td>
            <td>
              <span v-if="mode === 'list' || editingTransaction.id !== t.id">{{ t.date }}</span>
              <input v-else type="date" class="form-control" v-model="editingTransaction.date">
            </td>
            <td>
              <span v-if="mode === 'list' || editingTransaction.id !== t.id">{{ t.type }}</span>
              <select v-else name="type" v-model="editingTransaction.type">
                <option value="E">Expense</option>
                <option value="I">Income</option>
              </select>
            </td>
            <td>
              <span v-if="mode === 'list' || editingTransaction.id !== t.id">{{ t.amount }}</span>
              <input v-else type="number" class="form-control" v-model="editingTransaction.amount">
            </td>
            <td>
              <span v-if="mode === 'list' || editingTransaction.id !== t.id">{{ t.description }}</span>
              <input v-else type="text" class="form-control" v-model="editingTransaction.description">
            </td>
            <td>
              <span v-if="mode === 'list' || editingTransaction.id !== t.id">{{ getCategoryName(t.category) }}</span>
              <select v-else name="category" v-model="editingTransaction.category">
                <option v-for="category in transactionCategories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>
            </td>
            <td>
              <button v-if="mode === 'list' || editingTransaction.id !== t.id" class="btn btn-sm btn-primary" @click="editTransaction(t)">Edit</button>
              <button v-else class="btn btn-sm btn-primary" @click="saveTransaction(t)">Save</button>
              <button class="btn btn-sm btn-danger" @click="deleteTransaction(t)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>

      <button class="btn btn-primary" @click="createTransaction()">Create Transaction</button>

      <div v-if="mode === 'new'">
        <h3>Create Transaction</h3>
        <form @submit.prevent="saveTransaction()">
          <div class="form-group">
            <label for="name">ID</label>
            <input type="text" class="form-control" v-model="editingTransaction.id" disabled>
          </div>
          <div class="form-group">
            <label for="name">Date</label>
            <input type="text" class="form-control" v-model="editingTransaction.date">
          </div>
          <div class="form-group">
            <label for="value">Type</label>
            <input type="text" class="form-control" v-model="editingTransaction.type">
          </div>
          <div class="form-group">
            <label for="value">Amount</label>
            <input type="text" class="form-control" v-model="editingTransaction.amount">
          </div>
          <div class="form-group">
            <label for="value">Description</label>
            <input type="text" class="form-control" v-model="editingTransaction.description">
          </div>
          <div class="form-group">
            <label for="category">Category</label>
            <select id="category" class="form-select" v-model="editingTransaction.category">
              <option v-for="category in transactionCategories" :key="category.id" :value="category.id">
                {{ category.name }}
              </option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary">Save</button>
          <button type="button" class="btn btn-danger" @click="cancelEdit()">Cancel</button>
        </form>
      </div>
    </div>
  </template>
<!-- <input type="text" class="form-control" v-model="editingTransaction.category"> -->

  <script>
  import axios from 'axios'

  const hostUrl = "http://127.0.0.1:8000"

  export default {
    data() {
      return {
        transactions: [],
        transactionCategories: [],
        mode: 'list',
        editingTransaction: null,
        editingTransactionID: null,
      }
    },
    mounted() {
      this.getTransactions();
      this.getTransactionCategories();
    },
    methods: {
        getTransactions() {
        axios.get(`${hostUrl}/transaction/`)
          .then(response => {
            this.transactions = response.data.sort((a,b) => b.date - a.date);
          })
      },
      createTransaction() {
        const currentDate = new Date().toISOString().slice(0,10);
        this.editingTransaction = {
            date: currentDate,
            type: 'E',
            amount: '0',
            description: '',
            category: '',
        };
        this.mode = 'new';
      },
      editTransaction(transaction) {
        this.mode = 'edit';
        this.editingTransaction = { ...transaction };
        console.log(this.editingTransaction);
      },
      deleteTransaction(transaction) {
        axios.delete(`${hostUrl}/transaction/${transaction.id}/`)
          .then(() => {
            // this.transactions = this.transactions.filter(i => i.id !== transaction.id)
            this.getTransactions();
          })
      },
      saveTransaction() {

        // console.log(Vue.version);

        const isNew = !this.editingTransaction.id;
        axios[isNew ? 'post' : 'put'](isNew ? `${hostUrl}/transaction/` : `${hostUrl}/transaction/${this.editingTransaction.id}/`, this.editingTransaction)
          .then(response => {
            const savedTransaction = response.data;
            if (isNew) {
              this.transactions.push(savedTransaction);
            } else {
              const index = this.transactions.findIndex(i => i.id === savedTransaction.id);
              // this.$set(this.transactions, index, savedTransaction);
              this.transactions[index] = {...savedTransaction};
            }
            this.editingTransaction = null;
            this.mode = 'list';
          })
      },
      cancelEdit() {
        this.editingTransaction = null;
        this.mode = 'list';
      },
      getTransactionCategories() {

        axios['get'](`${hostUrl}/transaction-category/`)
          .then(response => {

            this.transactionCategories = response.data;
            // console.log(this.transactionCategories);

          })
      },
      getCategoryName(categoryId) {
        const categoryName = this.transactionCategories.find(cat => cat.id === categoryId);
        return categoryName ? categoryName.name : 'UNDEFINED';

      },
    }
  }

  </script>
